import StateMachine from '../utils/machine'
import {request, setHeader, removeHeader} from '../libs/axios'
import {setToken, removeToken} from '../libs/store'

const user = {
    namespaced: true,
    state: {
        token: '',
        data: null,
        machine: new StateMachine(),
        error: '',
        notify: {
            info: null,
            ready: false
        }
    },
    actions: {
        async updateBookmark(context, {username, bookmark, flag}) {
            await request({
                context,
                method: 'patch',
                payload: {
                    bookmark, flag
                },
                url: `users/${username}/`,
            })
        },
        async authenticate(context, credentials) {
            // Request token from server
            await request({
                context,
                method: 'post',
                url: 'auth/token/create/',
                payload: credentials,
                mutations: ['SET_TOKEN'],
                chain: true
            })

            // You'll always want to load user data after
            // authenticating, so this is called here.
            if (context.getters.GET_STATE !== 'handling') {
                await context.dispatch('load')
            }
        },
        async restore(context, token) {
            // Restore token from local storage
            if (token) {
                context.commit('SET_TOKEN', {auth_token: token})
                await context.dispatch('load')

                // Delete the token if we get a 401
                if (context.getters.GET_ERROR.status === 401) {
                    context.commit('REMOVE_TOKEN')
                    context.commit('SET_DATA')
                    context.commit('SET_ERROR')
                }
            }
        },
        async load(context) {
            // Request user data
            let user_info = null
            await (
                request({
                    context,
                    method: 'get',
                    url: 'auth/me/',
                    complete: response => {
                        user_info = response ? response.data : null
                    }
                })
            )
            await request({
                context,
                method: 'get',
                url: `users/${user_info.username}/`,
                mutations: ['SET_DATA']
            })
        },
        async deauthenticate(context) {
            // Destroy token
            await request({
                context,
                method: 'post',
                url: 'auth/token/destroy/',
                mutations: ['REMOVE_TOKEN', 'SET_DATA']
            }).then(
                removeToken()
            )
        },
        async register(context, payload) {
            await request({
                context,
                method: 'post',
                url: 'auth/users/create/',
                payload,
                mutations: ['SET_DATA']
            })
        },
        async loadNotifications(context) {
            await request({
                context,
                method: 'get',
                url: 'notify/',
                mutations: ['SET_NOTIFY'],
                // root: true
            })
        },
        async createNotification(context, {text, link, send_to, chain = false}) {
            await request({
                context,
                method: 'post',
                url: 'notify',
                payload: {
                    text, link, send_to
                },
                mutations: ['SET_NOTIFY'],
                chain
            })
        }
    },
    getters: {
        GET_NOTIFY: state => state => {
            if (state.notify.info) {
                return state.notify.info
            } else {
                return []
            }
        },
        GET_STATE: state => state.machine.state,
        GET_ERROR: state => state.error,
        GET_AUTHENTICATION: state => (!!state.token),
        GET_USER: state => state.data,
        GET_USERNAME: state => {
            if (state.data) {
                return state.data.username
            } else {
                return ''
            }
        },
        GET_TOKEN: state => state.token,
        GET_AVATAR: state => state.data.avatar,
        GET_BOOKMARK: state => state.data.bookmark,
        GET_THREADS: state => {
            if (state.data) {
                return state.data.posts
            } else {
                return []
            }
        }
    },
    mutations: {
        SET_NOTIFY(state, notify) {
            state.notify.info = notify
            state.notify.ready = true
        },
        SET_TOKEN(state, {auth_token}) {
            state.token = auth_token
            setToken(auth_token)
            setHeader('Authorization', `Token ${auth_token}`)
        },
        REMOVE_TOKEN(state) {
            state.token = ''
            removeToken()
            removeHeader('Authorization')
        },
        SET_DATA(state, data = {}) {
            state.data = data
        },
        SET_ERROR(state, message = '') {
            state.error = message
        },
        SET_STATE(state, action) {
            state.machine.do(action)
        }
    }
}

export default user
