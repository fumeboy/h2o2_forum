<template>
    <div class="box" :class="{'grid' : !editMode}">
        <header v-if="!editMode" class="header">
            <router-link :to="`/_${board}/${thread.id}/`">
                <h2 class="title">{{ thread.title }}</h2>
            </router-link>
            <h3 class="subtitle">Posted by
                <router-link :to="`/~${thread.author}`">{{ thread.author }}</router-link>
                {{ thread.created | timeElapsed }}
            </h3>
        </header>

        <thread-controls v-if="!editMode & have_marked[0]" :marked="have_marked[1]" :edit-allowed="editAllowed" :drawer-open="drawerOpen"
                         @toggle="drawerOpen = !drawerOpen" @bookmark="bookmarkOp" @delete="deleteThread"
                         @edit="editThread"/>

        <thread-editor v-if="editMode" :board="board" :thread="thread" @close="updateThread"/>

        <sliding-drawer :hidden="editMode" :drawer-open="drawerOpen" :refresh="refresh"
                        @refreshed="refresh = false">
            <article class="can-edit can-break" v-html="thread.content"></article>
        </sliding-drawer>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex'
    import './ThreadEditor'
    import './ThreadControls'

    export default Vue.component('thread-card', {
        props: {
            board: {
                type: String,
                required: true
            },
            thread: {
                type: Object,
                required: true
            }
        },
        data() {
            return {
                drawerOpen: false,
                editMode: false,
                refresh: false,
            }
        },
        computed: {
            have_marked: function () {
                let flag = 0
                let flag_2 = 0
                if (this.bookmark) {
                    flag = 1
                    flag_2 = this.bookmark.indexOf(this.thread.id) !== -1
                }
                return [flag, flag_2]
            },
            editAllowed: function () {
                return this.username === this.thread.author
            },
            handling: state => state === 'handling',
            ...mapGetters({
                username: 'user/GET_USERNAME',
                state: 'thread/GET_STATE',
                token: 'user/GET_TOKEN',
                bookmark: 'user/GET_BOOKMARK',
            })
        },
        watch: {
            editMode: function (val) {
                if (!val) this.refresh = true
            },
            thread: function () {
                this.refresh = true
            }
        },
        methods: {
            async bookmarkOp() {
                let flag = 2
                let a = this.bookmark.indexOf(this.thread.id)
                if (a === -1) flag = 1

                await this.$store.dispatch('user/updateBookmark', {
                    username: this.username,
                    flag: flag,
                    bookmark: this.thread.id
                }).then(() => {
                    if (flag === 1) {
                        this.bookmark.push(this.thread.id)
                    } else {
                        this.bookmark.splice(a, 1)
                    }
                })
            },
            deleteThread: async function () {
                if (confirm(`Are you sure you want to delete ${this.thread.title}?`)) {
                    await this.$store.dispatch('thread/deleteThread', {
                        board: this.board,
                        thread: this.thread.id
                    })

                    if (!this.handling) {
                        this.$emit('close')
                        await this.$store.dispatch('board/loadThreads')
                    }
                }
            },
            editThread: function () {
                this.drawerOpen = true
                this.editMode = true
            },
            updateThread: function () {
                this.editMode = false
                this.drawerOpen = true
            }
        }
    })
</script>

<style lang="sass">
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
