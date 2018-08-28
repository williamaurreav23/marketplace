import Vue from 'vue'
import Transformer from '../../base/transformers/BaseTransformer'
import Alert from '../models/Alert'

class AlertTransformer extends Transformer {
  static fetch (alert) {
    return new Alert({
      id: alert.id,
      rule: alert.rule,
      amount: alert.amoun,
      athlete: alert.athlete,
    })
  }
}

export default AlertTransformer
