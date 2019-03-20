import Router from 'vue-router'

import Forum from '../components/containers/Forum'
import Board from '../components/containers/Board'
import Thread from '../components/containers/Thread'
import Profile from '../components/containers/Profile'
import Bookmark from '../components/containers/Bookmark'

Vue.use(Router)

const routes = [
    {
        name: 'forum',
        path: '/',
        component: Forum
    },
    {
        name: 'board',
        path: '/_:board/',
        component: Board
    },
    {
        name: 'thread',
        path: '/_:board/:thread/',
        component: Thread
    },
    {
        name: 'profile',
        path: '/~:username',
        component: Profile,
    },
    {
        name: 'bookmark',
        path: '/~:username/bookmark/',
        component: Bookmark,
    }
]

const router = new Router({
    mode: 'history',
    /// #if PRODUCTION
    base: '/forum-app/',
    /// #endif
    routes,
    scrollBehavior(to, from, savedPosition) {
        return savedPosition ? savedPosition : {x: 0, y: 0}
    }
})
router.afterEach(async () => {
    console.log(router.app.$store.state.user)
    if (router.app.$store.state.user.data) {
        console.log(111)
        await router.app.$store.dispatch('user/loadNotifications')
    }
})

export default router
