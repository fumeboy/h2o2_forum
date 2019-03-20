<template>
    <div class="main">
        <thread-card :board="thread.board" :thread="thread" />
        <comment-list :thread="thread"></comment-list>
    </div>
</template>

<script>
    import '../parts/thread/ThreadControls'
    import '../parts/comment/CommentList'

    export default Vue.component('thread-view', {
        props: {
            thread: {
                required: true,
                type: Object,
                default: () => ({
                    title: '',
                    author: '',
                    created: 0,
                    content: ''
                })
            },
            comments: {
                required: true,
                type: Array,
                default: () => []
            }
        }
    })
</script>

<style lang="sass" scoped>
    header
        padding:
            left: 1.5rem
            right: 1.5rem
</style>
