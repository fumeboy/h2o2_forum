import StateMachine from '../utils/machine'
import {request} from '../libs/axios'

const comment = {
    namespaced: true,
    state: {
        data: {},
        comments: [],
        machine: new StateMachine(),
        error: ''
    },
    actions: {
        async loadComment(context, {board, thread}) {
            // Get Comment
            await request({
                context,
                method: 'get',
                url: `boards/${board}/threads/${thread}/comments/`,
                mutations: ['SET_COMMENT'],
                root: true
            })
        },
        async createComment(context, {board, thread, content, chain = false}) {
            // Post comment
            await request({
                context,
                method: 'post',
                url: `boards/${board}/threads/${thread}/comments/`,
                payload: {
                    thread: thread,
                    author: context.rootState.user.data.username,
                    content: content
                },
                mutations: ['SET_COMMENT'],
                chain
            })
        },
        async deleteComment(context, {board, thread, comment}) {
            // Delete comment
            await request({
                context,
                method: 'delete',
                url: `boards/${board}/threads/${thread}/comments/${comment}/`,
                mutations: ['SET_COMMENT']
            })
        },
        async updateComment(context, {board, thread, comment, content, chain = false}) {
            await request({
                context,
                method: 'patch',
                payload: {content},
                url: `boards/${board}/threads/${thread}/comments/${comment}/`,
                mutations: ['SET_COMMENT'],
                chain
            })
        }
    },
    getters: {
        GET_STATE: state => state.machine.state,
        GET_ERROR: state => state.error,
        GET_COMMENT: state => state.data
    },
    mutations: {
        SET_COMMENT(state, comment) {
            state.data = comment
        },
        SET_ERROR(state, message) {
            state.error = message
        },
        SET_STATE(state, action) {
            state.machine.do(action)
        }
    }
}

export default comment
