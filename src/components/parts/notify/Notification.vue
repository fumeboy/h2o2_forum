<template>
    <div class="notify">
        <div class="notify__phone" :class="{'notify__phone-active':if_show_notification}">
            <div class="notify__screen-wrapper">
                <div class="notify__screen">
                    <div class="notify__controls">
                        <div class="notify__arrow" @click="if_show_notification=!if_show_notification">
                            <i class="fa fa-chevron-left"></i>
                        </div>
                        <div class="notify__caption">Message</div>
                        <div class="notify__edit" @click="showModal=!showModal">
                            <i class="fa fa-edit"></i>
                        </div>
                    </div>
                    <div v-if="$store.state.user.notify.ready">
                        <div class="notify__card" v-for="one in $store.state.user.notify.info.results" :key="one.text">
                            {{one.text}}
                            <span>{{ one.created | timeElapsed }}</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="notify__notch"></div>
        </div>
        <notify-modal v-show="showModal" @close="showModal = false"/>
    </div>
</template>

<script>
    import BUS from '@libs/bus.js'
    import {mapGetters} from 'vuex'
    import './NotifyModal'

    export default {
        name: 'notify',
        computed: mapGetters({
            notify: 'user/GET_NOTIFY',
            error: 'GET_ERROR'
        }),
        methods: {
            show_notification() {
                this.if_show_notification = !this.if_show_notification
            },
        },
        created() {
            console.log(this.$store.getters)
            let a = this.notify
            BUS.register('show_notification', this.show_notification)
        },
        data() {
            return {
                showModal: false,
                if_show_notification: false,
            }
        }
    }
</script>

<style lang="scss" scoped>
    $resX: 1125px;
    $resY: 2436px;
    $notch-height: 90px;
    $notch-width: 627px;
    $notch-border-radius: 60px;
    $bezels: 48px;
    $screen-border-radius: 120px;
    $phone-border-radius: 160px;
    $scale: 4;

    $iphone-color: #120d30;
    $notch-color: $iphone-color;
    $screen-background: linear-gradient(#a25695, #5e4a9d);
    $indicators-color: white;

    *, *:before, *:after {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    .notify {
        &__phone-active {
            bottom: -($resY + $bezels * 2) / ($scale*6) !important;
            right: ($resX + $bezels * 2) / ($scale*10) !important;
        }

        &__phone {
            box-shadow: 0 0 120px rgba(74, 74, 74, 0.59);
            transition: all ease-in-out .6s;
            position: fixed;
            bottom: -2*($resY + $bezels * 2)/ ($scale);
            right: -2*($resX + $bezels * 2) / $scale;
            transform: rotate(1deg);
            width: ($resX + $bezels * 2) / $scale;
            height: ($resY + $bezels * 2) / $scale;
            padding-top: 1px;
            background-color: $iphone-color;
            border-radius: $phone-border-radius / $scale;
        }

        &__card {
            padding: 10px 10px;
            background: #f3f3f3;
            position: relative;
            margin: 10px 20px;
            min-height: 45px;
            border-radius: 6px;

            span {
                font-size: 80%
            }
        }

        &__card:before {
            content: '';
            position: absolute;
            left: -14px;
            top: 18px;
            border-style: solid;
            border-width: 4px 16px 10px 0;
            border-color: rgba(0, 0, 0, 0) #F3F3F3 rgba(0, 0, 0, 0) rgba(0, 0, 0, 0);
        }

        &__notch {
            position: absolute;
            top: $bezels / $scale;
            left: (($resX - $notch-width) / 2 + $bezels) / $scale;

            height: $notch-height / $scale;
            width: $notch-width / $scale;

            background-color: $notch-color;

            border-radius: 0 0 $notch-border-radius / $scale $notch-border-radius / $scale;
        }

        &__screen {
            position: relative;

            height: $resY / $scale;
            width: $resX / $scale;

            padding-top: 100px / $scale;

            background: $screen-background;

            border-radius: $screen-border-radius / $scale;
            cursor: grab;
            user-select: none;
            perspective: 700px;
        }

        &__screen-wrapper {
            position: relative;

            height: $resY / $scale;
            width: $resX / $scale - 6px;
            margin: $bezels / $scale + 3px;
            overflow: hidden;

            border-radius: $screen-border-radius / $scale;
        }

        &__controls {
            position: relative;
            display: flex;
            justify-content: center;

            padding: 25px / $scale 0;

            font-size: 75px / $scale;

            color: $indicators-color;
        }

        &__arrow {
            position: absolute;
            left: 60px / $scale;
        }

        &__edit {
            position: absolute;
            right: 60px / $scale + 10px;
        }


    }

    .animation {
        transition: transform 0.5s cubic-bezier(.55, .26, .12, 1.19);
    }

    .short-animation {
        transition: transform .2s ease;
    }

</style>