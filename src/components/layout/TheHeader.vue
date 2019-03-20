<template>
    <nav class="navbar is-radiusless" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item">
                <span class="icon is-large">
                    <i class="fa fa-hourglass-o fa-2x" />
                </span>
                <h1 class="title">{{title}}</h1>
            </router-link>
            <div v-if="!auth" class="navbar-item is-hidden-mobile">
                <button @click="showLogin = !showLogin" class="button is-info login-btn">
                    <span class="icon">
                        <i class="fa fa-sign-in" />
                    </span>
                    <span>Login</span>
                </button>
            </div>
            <button :class="{'is-active' : openDrawer}" class="button navbar-burger is-large is-white has-text-grey-darker" @click="openDrawer = !openDrawer" data-target="navMenu">
                ≡
                <div class="is-accessible">Open Navigation Drawer</div>
            </button>

        </div>
        <sliding-drawer :drawer-open="openDrawer" :refresh="refresh" @refreshed="refresh = false" classes="navbar-menu is-active">
            <div class="navbar-start" key="everyone">
                <a @click="showLogin = !showLogin" v-if="!auth" class="navbar-item is-primary is-hidden-tablet">Login</a>
                <a class="navbar-item">Trending</a>
                <a class="navbar-item">Browse</a>
            </div>
            <div v-if="auth" class="navbar-end" key="user">
                <router-link :to="`/~${username}`" class="navbar-item">Profile</router-link>
                <a class="navbar-item">Notifications</a>
                <a class="navbar-item">Bookmarks</a>
                <a class="navbar-item" @click="logout">Logout</a>
            </div>
        </sliding-drawer>
        <div class="navbar-menu" v-show="!openDrawer">
            <div class="navbar-start">
                <a @click="showLogin = !showLogin" v-if="!auth" class="navbar-item is-primary is-hidden-tablet">Login</a>
                <a class="navbar-item">Trending</a>
                <a class="navbar-item">Browse</a>
            </div>
            <div v-if="auth" class="navbar-end">
                <a class="navbar-item" @click="show_n">Notifications</a>
                <router-link :to="`/~${username}`" class="navbar-item">Profile</router-link>
                <router-link :to="`/~${username}/bookmark/`" class="navbar-item">Bookmark</router-link>
                <a class="navbar-item" @click="logout">Logout</a>
            </div>
        </div>
        <transition name="fade">
            <user-modal v-if="showLogin" @close="showLogin = false" />
        </transition>
    </nav>
</template>

<script>
import { mapGetters } from 'vuex'
import '../parts/login/UserModal'
import '../abstract/SlidingDrawer'
import BUS from '@libs/bus.js'

export default Vue.component('the-header', {
    data() {
        return {
            title:"H2O2",
            openDrawer: false,
            showLogin: false,
            refresh: false
        }
    },
    computed: mapGetters('user', {
        auth: 'GET_AUTHENTICATION',
        username: 'GET_USERNAME'
    }),
    watch: {
        auth: function() {
            this.refresh = true
        }
    },
    methods: {
        show_n(){
          BUS.invoke('show_notification')
        },
        logout: function() {
            this.$store.dispatch('user/deauthenticate')
        }
    }
})
</script>

<style lang="sass">

.navbar-burger
    height: 2em
    margin-top: .4rem
    margin-right: 1rem
</style>