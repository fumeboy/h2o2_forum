<template>
    <div class="comment-list" v-if="ready" ref="comment_list">
            <comment-card v-for="comment of comments" :comment="comment" :thread="thread" :key="comment.id"/>
    </div>
</template>

<script>
    import './CommentCard'
    import {mapGetters} from 'vuex'

    export default Vue.component('comment-list', {
        props: {
            thread: {
                type: Object,
                required: true
            }
        },
        data() {
            return {
                ready: false,
                refresh: false
            }
        },
        computed: mapGetters({
            comments: 'thread/GET_COMMENTS'
        }),
        watch: {
            comments: function () {
                this.refresh = true
            }
        },
        methods: {
            push_comment(author, content, time) {
                this.comments.push({
                    'author': author,
                    'content': content,
                    'created': time
                })
            }
        },
        async created() {
            await this.$store.dispatch('thread/loadComments').then(() => {
                this.ready = true
            })
        }
    })
</script>

