<template>
    <div class="avatar_grid">
        <div class="avatar-area">
            <div class="avatar_3d_paper_1">
                <div class="avatar-area__child"
                     v-for="(one,i) in code_1" :key="i"
                     :style="color(one)"></div>
            </div>
            <div class="avatar_3d_paper_2">
                <div class="avatar-area__child"
                     v-for="(one,i) in code_2" :key="i"
                     :style="color(one)"></div>
            </div>
            <div class="avatar_3d_paper_3">
                <div class="avatar-area__child"
                     v-for="(one,i) in code_3" :key="i"
                     :style="color(one)"></div>
            </div>
        </div>
        <div class="text">
            <h1 class="title">{{ user.username }}</h1>
            <h2 class="subtitle is-5">Joined on {{ user.date_joined | readableDate }}</h2>
        </div>
    </div>
</template>

<script>
    export default Vue.component('avatar', {
        props: [
            'user'
        ],
        computed: {
            color() {
                return function (code) {
                    return 'background:' + this.color_table[code]
                }
            }
        },
        methods: {
            get_code() {
                let temp = this.user.avatar
                if (temp.length > 192) temp = temp.substring(0, 191)
                else if (temp.length < 192) while (1) {
                    temp += '0'
                    if (temp.length === 192) break
                }
                this.code_1 = temp.substring(0, 64)
                this.code_2 = temp.substring(64, 128)
                this.code_3 = temp.substring(128, 192)
            }
        },
        data() {
            return {
                code_1: null,
                code_2: null,
                code_3: null,
                color_table: {
                    '0': '#000000',
                    '1': '#FF00FF',
                    '2': '#FA8072',
                    '3': '#800080',
                    '4': '#000080',
                    '5': '#008000',
                    '6': '#808000',
                    '7': '#800000',
                    '8': '#C0C0C0',
                    '9': '#808080',
                    'A': '#0000FF',
                    'B': '#00FFFF',
                    'C': '#00FF00',
                    'D': '#FFFF00',
                    'E': '#FF0000',
                    'F': '#FFFFFF'
                }

            }
        },
        created() {
            this.get_code()
        }
    })
</script>
