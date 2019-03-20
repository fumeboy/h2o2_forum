<template>
    <div class="sidebar">
        <div class="content">
            <h1 class="title">Welcome to H2O2</h1>
            <p>A forum with magic power.</p>
            <div class="stats_box">
                <div class="box__header">
                    <span class="box__header-title">stats</span>
                </div>
                <div class="box__body">
                    <div class="stats stats--main">
                        <div class="stats__amount">{{ stats.users }}</div>
                        <div class="stats__caption">users</div>
                    </div>

                    <div class="stats">
                        <div class="stats__amount">{{ stats.boards }}</div>
                        <div class="stats__caption">boards</div>
                    </div>

                    <div class="stats">
                        <div class="stats__amount">{{ stats.threads }}</div>
                        <div class="stats__caption">threads</div>
                    </div>

                    <div class="stats">
                        <div class="stats__amount">268</div>
                        <div class="stats__caption">likes</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default Vue.component('forum-sidebar', {
        props: {
            stats: {
                type: Object,
                required: true,
                default: () => ({})
            }
        }
    })
</script>