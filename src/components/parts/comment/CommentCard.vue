<template>
    <div class="box" :class="{'grid2' : !editMode}">
        <div class="header">
            <span>{{comment.author}}</span>
            <a class="hidden_link" :name="`${comment.id}`">a</a>
        </div>
        <comment-editor v-if="editMode" :thread="thread" :comment="comment" @close="updateComment()"/>

        <article class="can-edit can-break" v-html="comment.content"></article>
        <comment-controls v-if="!editMode" :edit-allowed="editAllowed"
                          @delete="deleteComment()"
                          @edit="editComment()"/>

    </div>
</template>

<script>
    import {mapGetters} from 'vuex'
    import './CommentEditor'
    import './CommentControls'

    export default Vue.component('comment-card', {
        props: {
            thread: {
                type: Object,
                required: true
            },
            comment: {
                type: Object,
                required: true
            }
        },
        data() {
            return {
                user: null,
                editMode: false,
                refresh: false
            }
        },
        computed: {
            editAllowed: function () {
                return this.username === this.comment.author
            },
            handling: state => state === 'handling',
            ...mapGetters({
                username: 'user/GET_USERNAME',
                avatar: 'user/GET_AVATAR',
                state: 'comment/GET_STATE'
            })
        },
        watch: {
            editMode: function (val) {
                if (!val) this.refresh = true
            },
            comment: function () {
                this.refresh = true
            }
        },
        methods: {
            deleteComment: async function () {
                if (confirm(`Are you sure you want to delete ${this.comment.title}?`)) {
                    await this.$store.dispatch('comment/deleteComment', {
                        board: this.thread.board,
                        thread: this.thread.id,
                        comment: this.comment.id
                    })

                    if (!this.handling) {
                        this.$emit('close')
                        await this.$store.dispatch('thread/loadComments')
                    }
                }
            },
            editComment: function () {
                this.editMode = true
            },
            updateComment: function () {
                this.editMode = false
            }
        }
    })
</script>

<style lang="sass">
    .hidden_link
        width: 0
        height: 0
        visibility: hidden

        .box.grid
            display: grid
            grid-template-columns: 1fr
            grid-template-rows: auto auto 1fr
            grid-template-areas: "header" "controls" "content"
            grid-row-gap: 1em

            .box.grid .header
                grid-area: header

            .box.grid .controls
                grid-area: controls

            .box.grid .content
                grid-area: content
</style>
