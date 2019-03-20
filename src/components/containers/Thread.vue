<template>
    <div class="view">
        <thread-view v-if="ready.view" :board="board(this.$route.params.board).slug" :thread="thread"
                     :comments="comments"/>
        <thread-sidebar v-if="ready.sidebar" :board="board(this.$route.params.board)" :thread="thread"
                        :authenticated="authenticated" :author="author"/>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex'
    import '../views/ThreadView'
    import '../sidebars/ThreadSidebar'
    import {request} from '@libs/axios'

    export default Vue.component('thread', {
        data() {
            return {
                author: null,
                ready: {
                    view: false,
                    sidebar: false
                }
            }
        },
        computed: mapGetters({
            comments: 'thread/GET_COMMENTS',
            thread: 'thread/GET_THREAD',
            board: 'board/GET_BOARD',
            authenticated: 'user/GET_AUTHENTICATION',
            error: 'GET_ERROR'
        }),
        methods: {
            getAuthor: async function () {
                await request({
                    method: 'get',
                    url: `users/${this.thread.author}/`,
                    complete: response => {
                        this.author = response ? response.data : null
                    }
                })
            },
        },
        async created() {
            // Get data
            this.$emit('progress', 0)
            await this.$store
                .dispatch('thread/loadThread', {
                    board: this.$route.params.board,
                    thread: this.$route.params.thread,
                }).then(() => {
                    this.$emit('progress', 50)
                })
            await this.$store.dispatch('board/loadBoard', {board: this.$route.params.board})
                .then(() => {
                    this.ready.view = true
                    this.$emit('progress', 80)
                })
            await this.getAuthor().then(() => {
                this.$emit('progress', 100)
                this.ready.sidebar = true
            })
        }
    })
</script>