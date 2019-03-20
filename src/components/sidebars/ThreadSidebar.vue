<template>
    <div class="sidebar">
        <router-link :to="`/_${board.slug}`">
            <h1 class="title">{{ board.name }}</h1>
        </router-link>
        <h2 class="subtitle">{{ board.description }}</h2>
        <avatar v-if="author" :user="author"></avatar>
        <button v-if="authenticated" class="button is-primary is-medium">
            <span class="icon">
                <i class="fa fa-plus"/>
            </span>
            <span @click="showPostModal = true">Reply the Thread</span>
        </button>
        <post-modal-c v-show="showPostModal" @close="showPostModal = false" :thread="thread"/>
    </div>
</template>

<script>
    import '../parts/profile/Avatar'
    import '../parts/comment/PostModal_C'

    export default Vue.component('thread-sidebar', {
        props: {
            board: {
                type: Object,
                required: true
            },
            thread: {
                required: true,
                type: Object
            },
            author: {
                required: true,
                type: Object
            },
            authenticated: {
                type: Boolean,
                required: true,
                default: false
            }
        },
        data: function () {
            return {
                showPostModal: false
            }
        }
    })
</script>