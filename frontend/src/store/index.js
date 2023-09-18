import { createStore } from 'vuex'
import page_data from "@/store/modules/page_data";
import burger from "@/store/modules/burger";

export default createStore({
  modules: {
    page_data,
    burger
  }
})
