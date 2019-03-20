<template>
    <transition name="fade">
        <div class="modal compose is-active">
            <div @click="$emit('close')" class="modal-background"></div>
            <div class="modal-card">
                <header class="modal-card-head">
                    <p class="modal-card-title">reply the Thread </p>
                    <button class="delete" aria-label="close" @click="$emit('close')"></button>
                </header>
                <section class="modal-card-body">
                    <div class="field">
                        <label for="who" class="label">@someone?</label>
                        <div class="control notify_box">
                            <input class="input" placeholder="Message Content" id="text" v-model="notify_text" type="text" value="">
                            <input class="input" placeholder="Send it to" id="who" v-model="notify_who" type="text" value="">
                            <input class="input" placeholder="a link with it" id="link" v-model="notify_link" type="text" value="">
                       </div>
                    </div>
                </section>
                <footer class="modal-card-foot">
                    <button @click="post" class="button is-success" :class="{'is-loading' : loading}">
                        <span class="icon">
                            <i class="fa fa-bolt"/>
                        </span>
                        <span>Reply</span>
                    </button>
                </footer>
            </div>
        </div>
    </transition>
</template>

<script>
    import {mapGetters} from 'vuex'
    export default Vue.component('notify-modal', {
        data: function () {
            return {
                notify_who:'',
                notify_text:'',
                notify_link:'',
            }
        },
        computed: {
            loading: function () {
                return this.state === 'loading'
            },
            ...mapGetters('user', {
                state: 'GET_STATE',
                error: 'GET_ERROR',
                notify: 'GET_NOTIFY'
            })
        },
        methods: {
            post: async function () {
                await this.$store.dispatch('user/createNotification', {
                    text: this.notify_text,
                    send_to: this.notify_who,
                    link: this.notify_link
                })
            }
        }
    })
</script>