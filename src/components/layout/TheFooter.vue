<template>
    <footer class="footer">
        <svg class="editorial"
             xmlns="http://www.w3.org/2000/svg"
             xmlns:xlink="http://www.w3.org/1999/xlink"
             viewBox="0 24 150 28"
             preserveAspectRatio="none">
            <defs>
                <path id="gentle-wave"
                      d="M-160 44c30 0
    58-18 88-18s
    58 18 88 18
    58-18 88-18
    58 18 88 18
    v44h-352z"/>
            </defs>
            <g class="parallax">
                <use xlink:href="#gentle-wave" x="50" y="0" fill="#D1F2EB"/>
                <use xlink:href="#gentle-wave" x="50" y="3" fill="#D5F5E3"/>
                <use xlink:href="#gentle-wave" x="50" y="6" fill="#A3E4D7"/>
            </g>
        </svg>
        <div class="content">
            <h1 contenteditable="true">X</h1>
        </div>

        <link href="https://fonts.googleapis.com/css?family=Lato:100" rel="stylesheet">

    </footer>
</template>

<script>
    import {mapState} from 'vuex'

    export default Vue.component('the-footer', {
        computed: mapState({
            board: state => state.board.data
        })
    })
</script>
<style lang="scss" scoped>
    .footer {
        background: transparent;
        height: 200px;
        padding: 0;
        margin: 20px;
        border-radius: 30px;
        color: #FFFFFA;
        overflow: hidden;
    }

    ::selection {
        background-color: salmon;
        color: white;
    }

    .parallax > use {
        animation: move-forever 12s linear infinite;

        &:nth-child(1) {
            animation-delay: -2s;
        }

        &:nth-child(2) {
            animation-delay: -2s;
            animation-duration: 5s
        }

        &:nth-child(3) {
            animation-delay: -4s;
            animation-duration: 3s
        }
    }

    @keyframes move-forever {
        0% {
            transform: translate(-90px, 0%)
        }
        100% {
            transform: translate(85px, 0%)
        }
    }


    .editorial {
        display: block;
        width: 100%;
        height: 10em;
        max-height: 100vh;
        margin: 0;
    }

    .content {
        font-family: 'Lato', sans-serif;
        text-align: center;
        background-color: #A3E4D7;
        min-height: 75vh;
        margin: -.1em 0 0 0;
        padding: 1em;
        color: #eee;
        font-size: 2em;
        font-weight: 300;
    }

    .content {
        font-size: 1em;
    }

    .content h1 {
        margin-top: -1.3em;
        font-weight: 100;
        font-size: 5em;
        user-select: none;
        cursor: default;
    }

    /*prevent many large-by-comparison ripples by shrinking the height*/
    @media (max-width: 50em) {
        .content h1 {
            font-size: 12vmax
        }
        .editorial {
            height: 17vw;
        }
    }

</style>