<template>
    <div class="sidebar">
        <div v-if="user" class="content">
            <div class="media">
                <avatar :user="user"></avatar>
            </div>
            <slot/>
        </div>
    </div>
</template>

<script>
    import '@parts/profile/ProfileControls'
    import '@parts/profile/Avatar'

    export default Vue.component('profile-sidebar', {
        props: {
            user: {
                type: Object,
                required: false,
                default: () => {
                }
            },
            isMe: {
                type: Boolean,
                required: false,
                default: false
            }
        }
    })
</script>

<style lang="sass" scoped>
    @import "~styles/main"

    .sidebar
        max-width: 400px

    .media-left
        height: 128px
        width: 128px

    .media-content
        height: 128px
        display: flex
        flex-flow: column nowrap
        justify-content: center
</style>
