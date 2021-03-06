<template>
  <el-col :xs="24" class="formSteps-container" v-loading.fullscreen.lock="loading">
    <div class="infoTag" v-if="campaign.isDraft">Draft Campaign</div>
    <el-breadcrumb separator=">">
      <el-breadcrumb-item :to="{ path: '/campaigns' }">Campaign</el-breadcrumb-item>
      <el-breadcrumb-item><a href="/campaigns/create">Funding</a></el-breadcrumb-item>
    </el-breadcrumb>
    <div class="formSteps-actions">
      <el-button v-if="campaign.isDraft" type="danger" class="" @click.prevent="$emit('discard')">{{
        $tc('message.DiscardCampaign') }}
      </el-button>
      <!-- <el-button type="secondary" class="" @click.prevent="onSaveAndContinue()">{{ $tc('message.ReviewLaunch') }}</el-button> -->
    </div>
    <div class="formSteps">
      <h2 class="formSteps-title">{{ $tc('message.Funding') }}</h2>
      <p class="formSteps-text">Raise funds for and achieve your dream</p>
      <el-form-item required :label="$tc('message.FundsRequirement')">
        <p class="formSteps-inputText">How much money you need?</p>
        <div class="formSteps-inputSelect">
          <vue-autonumeric class="autonumeric" :options="''" v-model="form.funds"></vue-autonumeric>
          <el-select v-model="form.currency" placeholder="Select">
            <el-option v-for="item in currencies" :key="item.value" :label="item.label" :value="item.value">
            </el-option>
          </el-select>
        </div>
      </el-form-item>
      <el-form-item required :label="$tc('message.HowYouUseFunds')">
        <p class="formSteps-inputText">(Hire a trainer, equipment, travel)</p>
        <el-input type="textarea" v-model="form.use"></el-input>
      </el-form-item>
      <el-form-item required :label="$tc('message.GiveBack')">
        <p class="formSteps-inputText">Express the magnitude of what contributors will help you achieve.</p>
        <el-input type="textarea" v-model="form.giveBack"></el-input>
      </el-form-item>
      <el-form-item required :label="$tc('message.RevenueFor')">
        <p class="formSteps-inputText">Express the magnitude of what contributors will help you achieve.</p>
        <div class="formSteps-containerInputSelect">
          <div v-for="(revenue, index) in form.revenues" :key="index" class="formSteps-inputSelect">
            <div class="formSteps-inputSelect-year">{{ revenue.year }}</div>
            <vue-autonumeric class="autonumeric" :options="''" v-model="revenue.amount"></vue-autonumeric>
            <el-select v-model="revenue.currency" placeholder="Select">
              <el-option v-for="item in currencies" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
          </div>
        </div>
      </el-form-item>
      <el-form-item required :label="$tc('message.IncomeFor')">
        <p class="formSteps-inputText">Express the magnitude of what contributors will help you achieve.</p>
        <div class="formSteps-containerInputSelect">
          <div v-for="(income, index) in form.incomes" :key="index" class="formSteps-inputSelect">
            <div class="formSteps-inputSelect-year">{{ income.year }}</div>

            <vue-autonumeric class="autonumeric" :options="''" v-model="income.amount"></vue-autonumeric>
            <el-select v-model="income.currency" placeholder="Select">
              <el-option v-for="item in currencies" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
          </div>
        </div>
      </el-form-item>
      <el-form-item required :label="$tc('message.Examples')">
        <p class="formSteps-inputText">Examples of income of other similar professionals of the same sport</p>
        <el-input type="textarea" v-model="form.examples"></el-input>
      </el-form-item>
      <el-form-item :label="$tc('message.Recommendations')">
        <p class="formSteps-inputText">Upload recommendation /reference letters from coaches/experts</p>
        <el-upload :action="options.action" :name="options.name" :headers="options.headers" :data="options.data"
                   :file-list="form.recommendations">
          <el-button size="small" type="secondary">Upload</el-button>
        </el-upload>
      </el-form-item>
      <el-form-item>
        <div class="formSteps-lineButton"></div>
        <el-button type="primary" class="is-uppercase" @click.prevent="onSaveAndContinue()">{{
          $tc('message.SaveContinue') }}
        </el-button>
        <el-button type="secondary" class="is-uppercase" @click.prevent="onLaunch()">Launch</el-button>
      </el-form-item>
    </div>
  </el-col>
</template>

<script type="text/babel">
  import Vue from 'vue'
  import { mapGetters } from 'vuex'
  import { Message } from 'element-ui'
  import router from '@/router.js'
  import VueAutonumeric from 'vue-autonumeric/src/components/VueAutonumeric.vue'

  export default {
    name: 'Funding',
    components: {
      VueAutonumeric
    },
    data () {
      return {
        // Form
        currencies: [{value: 'USD', label: 'USD'}],
        form: {
          currency: 'USD',
          funds: null,
          use: null,
          giveBack: null,
          revenues: [],
          incomes: [],
          examples: null,
          recommendations: []
        },
        options: {
          action: `${Vue.axios.defaults.baseURL}/api/v1/recommendations/`,
          name: 'file',
          headers: {
            Authorization: this.$store.getters['auth/header']
          }
        },
        loading: false
      }
    },
    computed: {
      ...mapGetters({
        campaign: 'campaigns/campaign',
        user: 'users/user'
      })
    },
    created () {
      this.loading = true
      this.$store
        .dispatch('campaigns/fetch', this.$route.params.campaignId)
        .then(() => {
          if (!!this.campaign && !!this.campaign.id) {
            this.options.data = {
              campaign: this.campaign.id
            }
            this.form = {...this.campaign}
            this.form.recommendations = this.campaign.recommendations.map(
              recomendation => {
                return {
                  name: recomendation.file.substring(
                    recomendation.file.lastIndexOf('/') + 1
                  ),
                  url: recomendation.file
                }
              }
            )
            this.form.revenues = this.initialRevenues(this.campaign)
            this.form.incomes = this.initialIncomes(this.campaign)
            if (!this.form.currency) {
              this.form.currency = 'USD'
            }
          }
          this.loading = false
        })
        .catch(() => router.push({name: 'campaign.create'}))
    },
    methods: {
      initialRevenues (campaign) {
        const currentYear = new Date().getFullYear()
        const initialRevenues = [...Array(3).keys()].map(diff => {
          return {
            id: null,
            campaign: this.campaign.id,
            year: currentYear - diff,
            amount: null,
            currency: 'USD'
          }
        })
        return initialRevenues.map(revenue => {
          const revenues = campaign.revenues.filter(
            item => item.year == revenue.year
          )
          if (revenues.length > 0) return revenues[0]
          return revenue
        })
      },
      initialIncomes (campaign) {
        const currentYear = new Date().getFullYear()
        const initialIncomes = [...Array(5).keys()].map(diff => {
          return {
            id: null,
            campaign: this.campaign.id,
            year: currentYear + diff + 1,
            amount: null,
            currency: 'USD'
          }
        })
        return initialIncomes.map(income => {
          const incomes = campaign.incomes.filter(
            item => item.year == income.year
          )
          if (incomes.length > 0) return incomes[0]
          return income
        })
      },
      onSaveAndContinue () {
        return new Promise((resolve, reject) => {
          this.loading = true
          const payload = {
            id: this.campaign.id,
            currency: this.form.currency,
            funds: this.form.funds,
            use: this.form.use,
            giveBack: this.form.giveBack,
            revenues: this.form.revenues,
            incomes: this.form.incomes,
            examples: this.form.examples
          }
          this.$store.dispatch('campaigns/update', payload).then(() => {
            this.form = {...this.campaign}
            this.loading = false
            resolve()
          }).catch(error => {reject(error)})
        })
      },
      getCampaignErrors () {
        // Check if the campaign has all the data
        const required = ['title', 'description', 'image', 'country', 'gender', 'sport', 'tags', 'height', 'weight', 'club', 'coach', 'ranking', 'funds', 'use', 'giveBack', 'revenues', 'incomes', 'examples']
        const errors = required.filter(field => !this.campaign[field])
        // Campaign must have either a pitch image or a pitch video
        if (!this.campaign.pitchImage && !this.campaign.pitchUrl) {
          errors.push('pitch')
        }
        return errors
      },
      launchCampaign () {
        return new Promise((resolve, reject) => {
          this.$store.dispatch('campaigns/update', {
            id: this.campaign.id,
            isDraft: false
          }).then((campaign) => {resolve(campaign)})
            .catch((error) => {reject(error)})
        })
      },
      onLaunch () {
        this.onSaveAndContinue()
          .then(() => {
            this.loading = true
            const errors = this.getCampaignErrors()
            if (errors.length === 0) {
              this.launchCampaign()
                .then((campaign) => {
                  router.push({
                    name: 'campaign.success',
                    params: {campaignId: this.campaign.id}
                  })
                }).catch(error => {
                console.error(errors)
              })
            } else {
              Message.error({
                message: 'You must complete the missing mandatory fields',
                center: true
              })
              console.error(errors)
              this.loading = false
            }
          })
      }
    }
  }
</script>

<style type="scss" scoped>
  .autonumeric {
    -webkit-appearance: none;
    background-color: #fff;
    background-image: none;
    border-radius: 4px;
    border: 1px solid #dcdfe6;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    color: #606266;
    display: inline-block;
    font-size: inherit;
    height: 40px;
    line-height: 40px;
    outline: none;
    padding: 0 15px;
    -webkit-transition: border-color 0.2s cubic-bezier(0.645, 0.045, 0.355, 1);
    transition: border-color 0.2s cubic-bezier(0.645, 0.045, 0.355, 1);
    max-width: 210px;
  }
</style>
