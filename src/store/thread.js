import StateMachine from '../utils/machine'
import { request } from '../libs/axios'

const thread = {
    namespaced: true,
    state: {
        data: {},
        comments: [],
        machine: new StateMachine(),
        error: ''
    },
    actions: {
        async loadComments(context, { params = false, chain = false } = {}) {
            let info = context.getters.GET_THREAD
            await request({
                context,
                method: 'get',
                url: `boards/${info.board}/threads/${info.id}/comments/${params ? params : ''}`,
                mutations: ['SET_COMMENTS'],
                root: true,
            })
        },
        async loadThread(context, { board ,thread}) {
            // Get thread
            await request({
                context,
                method: 'get',
                url: `boards/${board}/threads/${thread}/`,
                mutations: ['SET_THREAD'],
                root: true
            })
        },
        async createThread(context, { board, title, content, chain = false }) {
            // Post thread
            await request({
                context,
                method: 'post',
                url: `boards/${board}/threads/`,
                payload: {
                    author: context.rootState.user.data.username,
                    board: board,
                    title: title,
                    content: content
                },
                mutations: ['SET_THREAD'],
                chain
            })
        },
        async deleteThread(context, { board }) {
            // Delete thread
            await request({
                context,
                method: 'delete',
                url: `boards/${board}/threads/${thread}/`,
                mutations: ['SET_THREAD']
            })
        },
        async updateThread(context, { board, thread, title, content, chain = false }) {
            await request({
                context,
                method: 'patch',
                payload: { title, content },
                url: `boards/${board}/threads/${thread}/`,
                mutations: ['SET_THREAD'],
                chain
            })
        }
    },
    getters: {
        GET_COMMENTS: state => state.comments,
        GET_STATE: state => state.machine.state,
        GET_ERROR: state => state.error,
        GET_THREAD: state => state.data
    },
    mutations: {
        SET_THREAD(state, thread) {
            state.data = thread
        },
        SET_ERROR(state, message) {
            state.error = message
        },
        SET_STATE(state, action) {
            state.machine.do(action)
        },
        SET_COMMENTS(state, comments) {
            Vue.set(state, 'comments', comments.results)
        }
    }
}

export default thread
