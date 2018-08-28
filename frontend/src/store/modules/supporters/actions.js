import Vue from 'vue'
import AlertTransformer from '../../../supporters/transformers/AlertTransformer'
import { store } from '../../index'


export default {
  alerts ({commit, state}, payload={}) {
    return new Promise((resolve, reject) => {
      const { url, filters, push } = payload
      let endpoint = state.endpoints.alerts
      if (!!url) {
        endpoint = url
      } else if (!!filters) {
        const query = Object.keys(filters).map(key => `${key}=${filters[key]}`).join('&')
        endpoint = [endpoint, query].join('?')
      }
      Vue.axios.get(endpoint).then((response) => {
        const { results, count, next, previous } = response.data;
        const alerts = results.map(item => AlertTransformer.fetch(item));
        if (push) {
          commit('pushAlerts', alerts)
        } else {
          commit('alerts', alerts)
        }
        commit('pagination', {count, next, previous})
        resolve(alerts)
      }).catch((error) => {
        reject(error)
      })
    })
  },

}
