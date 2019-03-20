<template>
    <div class="view">
        <profile-view v-if="ready" :user="user" :threads="threads_list.list"/>
        <profile-sidebar v-if="ready" :user="user" :is-me="is_me">
            <profile-bio @save="setBio" @cancel="edit = false" :bio="user.bio" :edit="edit"
                         :is-me="is_me"/>
        </profile-sidebar>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex'
    import {request} from '@libs/axios'
    import '@parts/profile/ProfileControls'
    import '@views/ProfileView'
    import '@parts/profile/ProfileBio'
    import '@sidebars/ProfileSidebar'

    export default Vue.component('profile', {
        data() {
            return {
                user: null,
                edit: false,
                ready: false,
                avatar: false,
                threads_list: null,
                is_me: false
            }
        },
        computed: {
            ...mapGetters({
                me: 'user/GET_USER',
                token: 'user/GET_TOKEN'
            })
        },
        async created() {
            this.$emit('progress', 0)
            if (!this.me) {
                await this.setUser().then(() => {
                    this.$emit('progress', 10)
                })
            } else {
                if (this.$route.params.username !== this.me.username) {
                    this.user = this.me
                    this.is_me = true
                } else {
                    await this.setUser().then(() => {
                        this.$emit('progress', 10)
                    })
                }
            }
            await this.getThreads().then(() => {
                this.$emit('progress', 100)
                this.ready = true
            })
        },
        methods: {
            getThreads: async function () {
                await request({
                    method: 'get',
                    url: `users/${this.$route.params.username}/threads/`,
                    complete: response => {
                        this.threads_list = response.data
                        console.log(response.data)
                    }
                })
            },
            setUser: async function () {
                await request({
                    method: 'get',
                    url: `users/${this.$route.params.username}/`,
                    complete: response => {
                        if(response){
                            this.user = response.data
                            this.is_me = true
                        }
                    }
                })
            },
            setBio: async function (bio, callComplete, callError) {
                await request({
                    method: 'patch',
                    url: `users/${this.$route.params.username}/`,
                    payload: {bio},
                    complete: () => {
                        this.user.bio = bio
                        this.edit = false
                        callComplete()
                    },
                    error: () => {
                        callError()
                    }
                })
            }
        }
    })
</script>

<style>

</style>
