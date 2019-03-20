<template>
    <div class="controls">
        <div>
            <button :disabled="disabled" @click="$emit('toggle')" class="button">
                <span class="icon">
                    <i class="fa" :class="{'fa-plus' : !drawerOpen, 'fa-minus' : drawerOpen}">
                        <span class="is-accessible" v-if="!drawerOpen">Open</span>
                        <span class="is-accessible" v-else>Close</span>
                    </i>
                </span>
            </button>
            <button :disabled="disabled" class="button" @click="$emit('bookmark')">
                <span class="icon">
                    <i class="fa fa-heart" :class="{'marked' : marked}">
                        <span class="is-accessible">Bookmark</span>
                    </i>
                </span>
            </button>
        </div>
        <div v-if="editAllowed">
            <button :disabled="disabled" @click="$emit('edit')" class="button">
                <span class="icon">
                    <i class="fa fa-pencil">
                        <span class="is-accessible">Edit</span>
                    </i>
                </span>
            </button>
            <button :disabled="disabled" @click="$emit('delete')" class="button">
                <span class="icon">
                    <i class="fa fa-trash">
                        <span class="is-accessible">Delete</span>
                    </i>
                </span>
            </button>
        </div>
    </div>
</template>

<script>
    export default Vue.component('thread-controls', {
        props: {
            editAllowed: {
                type: Boolean,
                required: false,
                default: false
            },
            drawerOpen: {
                type: Boolean,
                required: false,
                default: true
            },
            disabled: {
                type: Boolean,
                required: false,
                default: false
            },
            marked:{
                type: Boolean,
                required: false,
                default: false
            }
        }
    })
</script>

<style lang="sass">
    .controls
        width: 100%
        display: flex
        flex-direction: row
        justify-content: space-between
</style>
