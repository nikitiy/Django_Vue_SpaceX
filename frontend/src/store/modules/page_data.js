import axios from "axios";

export default {
  state: {
    header_navigations: [
        {
            id: 1,
            title: "",
            link: ""
        },
    ],
    adventages: [
        {
            id: 1,
            adventage_row_1: "",
            adventage_row_2: "",
            adventage_row_3: "",
        },
    ],
  },
  getters: {
    header_navigations_data(state) {return state.header_navigations;},
    adventages_data(state) {return state.adventages;},

  },
  mutations: {
    UpdateHeaderNavigations(state, values) {
        state.header_navigations = values;
    },
    UpdateAdventages(state, values) {
        state.adventages = values;
    },
  },
  actions: {
    async getPageData(ctx) {
        await axios
          .get('/api/v1/header_navigations/')
          .then(response => ctx.commit('UpdateHeaderNavigations', response.data));
        await axios
          .get('/api/v1/adventages/')
          .then(response => ctx.commit('UpdateAdventages', response.data));
    }
  }
}
