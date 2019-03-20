<template>
    <div class="controls">
        <div>
            <button :disabled="disabled" class="button">
                <span class="icon">
                    <i class="fa fa-link">
                        <span class="is-accessible">Copy Link</span>
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
    export default Vue.component('comment-controls', {
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
