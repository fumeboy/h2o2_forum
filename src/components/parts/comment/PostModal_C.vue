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
                    <div class="field">
                        <label for="content" class="label">Content</label>
                        <div class="control" id="content">
                            <vue-editor v-model="content"></vue-editor>
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
                    <p v-if="error" class="help is-danger">
                        {{ error.data.content.toString() }}
                    </p>
                </footer>
            </div>
        </div>
    </transition>
</template>

<script>
    import {mapGetters} from 'vuex'
    import {VueEditor} from 'vue2-editor'

    export default Vue.component('post-modal-c', {
        components: {
            VueEditor
        },
        props: {
            thread: {
                type: Object,
                required: true
            },
        },
        data: function () {
            return {
                content: '',
                notify_who:'',
                notify_text:'',
                notify_link:'',
            }
        },
        computed: {
            loading: function () {
                return this.state === 'loading'
            },
            ...mapGetters('comment', {
                state: 'GET_STATE',
                error: 'GET_ERROR',
                comment: 'GET_COMMENT'
            })
        },
        methods: {
            post: async function () {
                console.log(this.thread)
                await this.$store.dispatch('comment/createComment', {
                    board: this.thread.board,
                    thread: this.thread.id,
                    content: this.content
                })

                if (!this.error) {
                    await this.$store.dispatch('thread/loadComments')
                    this.$emit('close')
                }
            }
        }
    })
</script>