<template>
    <main class="main">
        <thread-card v-for="thread in threads" :key="thread.name" :board="thread.board" :thread="thread" />
        <div v-if="user && threads.length === 0">
            <p class="title">
                This user hasn't marked any threads.
            </p>
        </div>
        <div v-if="!user">
            <p class="title">
                Oh no, 404! This user doesn't exist.
            </p>
        </div>
    </main>
</template>

<script>
import '../parts/thread/ThreadCard'

export default Vue.component('bookmark-view', {
    props: {
        threads: {
            type: Array,
            required: false,
            default: () => []
        },
        user: {
            type: Object,
            required: false,
            default: () => {}
        }
    }
})
</script>