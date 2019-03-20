<template>
    <main class="main">
        <div v-if="boards.length > 0" class="grid">
            <board-card v-for="board in boards" :auth="auth" :key="board.name" :board="board" @remove="removeBoard"/>
        </div>
        <div v-else-if="auth">
            <h1 class="title">Create new boards !</h1>
        </div>
        <div class="grid">
            <div class="card spe-card" v-for="(card,i) in cards" :key="i">
                <div class="spe-card__line_1">{{card.text_1}}</div>
                <div class="spe-card__line_2">{{card.text_2}}</div>
            </div>
        </div>
    </main>
</template>

<script>
    import '../parts/BoardCard'
    import '../parts/GreatNotice'

    export default Vue.component('forum-view', {
        data() {
            return {
                cards: [
                    {
                        text_1: 'City',
                        text_2: 'NanChang'
                    },
                    {
                        text_1: 'Lucky',
                        text_2: 'Max'
                    },
                    {
                        text_1: 'Weather',
                        text_2: 'Great'
                    },
                ]
            }
        },
        props: {
            boards: {
                type: Array,
                required: true
            },
            auth: {
                type: Boolean,
                required: true
            }
        },
        methods: {
            removeBoard: function (boardName) {
                this.$emit('remove', boardName)
            }
        }
    })
</script>
<style lang="scss" scoped>
    .spe-card {
        position: relative;
    }

    .spe-card:nth-child(1) {
        background: #D1F2EB;
    }

    .spe-card:nth-child(2) {
        background: #D5F5E3;
    }

    .spe-card:nth-child(3) {
        background: #A3E4D7;
    }

    .spe-card__line_1 {
        font-weight: 300;
        position: absolute;
        top: 10px;
        left: 10px;
        color: #000;
        font-size: 36px;
    }

    .spe-card__line_2 {
        font-weight: 400;
        position: absolute;
        bottom: 10px;
        right: 10px;
        color: #000;
        font-size: 36px;
    }
</style>