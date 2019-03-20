<template>
    <div class="view">
        <bookmark-view v-if="ready" :user="user" :threads="threads_list.list"/>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex'
    import {request} from '@libs/axios'
    import '@views/BookmarkView'

    export default Vue.component('profile', {
        data() {
            return {
                user: null,
                edit: false,
                ready: false,
                avatar: false,
                threads_list: null
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
                    url: `users/${this.$route.params.username}/bookmark/`,
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
                        this.user = response ? response.data : null
                    }
                })
            }
        }
    })
</script>

<style>

</style>
