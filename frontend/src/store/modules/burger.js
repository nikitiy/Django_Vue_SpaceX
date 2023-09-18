export default {
    state: {
        burger_isShow: false,
    },
    getters: {
        getBurgerStatus(state) {
            return state.burger_isShow;
        }
    },
    mutations: {
        UpdateBurgerStatus(state, status) {
            state.burger_isShow = status;
        }
    },
    actions: {
        ChangeBurgerStatus(ctx, status) {
            ctx.commit('UpdateBurgerStatus', status);
        }
    }
}
