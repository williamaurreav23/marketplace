<template>
  <gb-base-layout>
    <el-row type="flex" justify="center" class="profile-info">
      <el-col :xs="24" :sm="12" :md="12" :lg="10" :xl="6" class="text-center">
        <h2 class="form-lined-title">{{ $tc("message.Profile") }}</h2>
        <div class="form-lined">
          <el-form ref="form" label-position="top" class="text-left" :model="form" :rules="rules">
            <el-row :gutter="20">
              <el-col :xs="24" :md="12">
                <el-form-item required prop="email">
                  <el-input v-bind:placeholder="$tc('message.Email')" type="email" v-model="form.email"></el-input>
                </el-form-item>
              </el-col>
              <el-col :xs="24" :md="12">
                <el-form-item prop="password">
                  <el-input v-bind:placeholder="$tc('message.Password')" type="password" v-model="form.password"></el-input>
                </el-form-item>
              </el-col>
              <el-col :xs="24" :md="12">
                <el-form-item prop="firstName">
                  <el-input v-bind:placeholder="$tc('message.FirstName')" type="text" v-model="form.firstName"></el-input>
                </el-form-item>
              </el-col>
              <el-col :xs="24" :md="12">
                <el-form-item prop="lastName">
                  <el-input v-bind:placeholder="$tc('message.LastName')" type="text" v-model="form.lastName"></el-input>
                </el-form-item>
              </el-col>
            </el-row>
            <el-form-item class="text-center">
              <el-button type="primary" class="is-uppercase" @click.prevent="onSubmit('form')">{{ $tc("message.Save") }}</el-button>
            </el-form-item>
          </el-form>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-col :xs="24" class="">
        <el-tabs type="border-card">
          <el-tab-pane :label="$tc('message.Following')">
            <el-table :data="campaigns" style="width: 100%">
              <el-table-column prop="id" label="ID"></el-table-column>
              <el-table-column prop="title" label="Title"></el-table-column>
              <el-table-column prop="sport.name" label="Sport"></el-table-column>
              <el-table-column fixed="right" label="Operaciones">
                <template slot-scope="scope">
                  <el-button @click="unfollow(scope)" type="text" size="small">{{$tc('message.Unfollow')}}</el-button>
                </template>
              </el-table-column>
            </el-table>
          </el-tab-pane>
          <el-tab-pane :label="$tc('message.Alert',2)">
            <el-table :data="alerts" style="width: 100%">
              <el-table-column prop="id" label="ID"></el-table-column>
              <el-table-column prop="rule" label="Rule"></el-table-column>
              <el-table-column prop="amount" label="Amount"></el-table-column>
              <el-table-column prop="athlete.firstName" label="Athlete"></el-table-column>
            </el-table>
          </el-tab-pane>
        </el-tabs>
      </el-col>
    </el-row>
  </gb-base-layout>
</template>

<script>
import BaseLayout from '@/layout/BaseLayout.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'Profile',
  components: {
    'gb-base-layout': BaseLayout
  },
  data() {
    return {
      form: {
        email: '',
        password: '',
        firstName: '',
        lastName: ''
      },
      rules: {
      }
    }
  },
  computed: {
    ...mapGetters({
      alerts: 'supporters/alerts',
      campaigns: 'campaigns/campaigns',
      pagination: 'campaigns/pagination',
      user: 'users/user'
    })
  },
  created() {
    this.initial()
  },
  methods: {
    initial() {
      this.$store.commit('campaigns/campaigns', [])
      this.$store.dispatch('supporters/alerts')
      this.$store.dispatch('users/fetchUser').then(user => {
        this.form = { ...this.user}
        this.$store.dispatch('campaigns/list', {
          filters: { followed_by: user.id }
        })
      })
    },
    unfollow(scope) {
      const id = scope.row.id
      this.$store
        .dispatch('athletes/follow', id)
        .then(() => {
          this.$store.dispatch('athletes/list', {
            filters: { followed_by: this.user.id }
          })
        })
        .catch(error => {
          console.log(error)
        })
    },
    onSubmit(form) {
      this.$refs[form].validate(valid => {
        if (valid) {
          const dataForm = Object.assign({}, this.form)
          this.saveUserProfile(dataForm)
        } else {
          return false
        }
      })
    },
    saveUserProfile(data) {
      this.$store
        .dispatch('users/update', data)
        .then(response => {
          console.log('Supporter updated')
        })
        .catch(error => {
          console.error(error)
        })
    }
  }
}
</script>

<style type="scss" scoped>
.profile-info {
  margin-bottom: 20px;
}
</style>