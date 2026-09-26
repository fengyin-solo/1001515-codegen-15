<template>
  <section class="page">
    <header class="page-head">
      <div>
        <h2>运营概览</h2>
        <p class="page-desc">汇总各业务模块的关键指标，先看总量再看异常。</p>
      </div>
    </header>
    <div class="stat-row">
      <article v-for="card in cards" :key="card.label" class="stat-card">
        <span class="stat-label">{{ card.label }}</span>
        <strong class="stat-value">{{ card.value }}</strong>
      </article>
    </div>
    <table class="data-table">
      <thead>
        <tr><th>业务模块</th><th>今日新增</th><th>待处理</th><th>异常量</th></tr>
      </thead>
      <tbody>
        <tr v-for="row in moduleRows" :key="row.name">
          <td>{{ row.name }}</td>
          <td>{{ row.created }}</td>
          <td>{{ row.pending }}</td>
          <td>{{ row.abnormal }}</td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { fetchJson } from '@/api/client'

type Overview = {
  cards: { label: string; value: number }[]
  modules: { name: string; created: number; pending: number; abnormal: number }[]
}

const cards = ref<Overview['cards']>([])
const moduleRows = ref<Overview['modules']>([])

onMounted(async () => {
  try {
    const payload = await fetchJson<Overview>('/api/overview')
    cards.value = payload.cards
    moduleRows.value = payload.modules
  } catch {
    cards.value = [{"label": "业务模块", "value": 0}, {"label": "今日新增", "value": 0}]
    moduleRows.value = [{"name": "航班信息", "created": 0, "pending": 0, "abnormal": 0}, {"name": "停机位分配", "created": 0, "pending": 0, "abnormal": 0}, {"name": "行李转运", "created": 0, "pending": 0, "abnormal": 0}, {"name": "廊桥调度", "created": 0, "pending": 0, "abnormal": 0}, {"name": "客梯车调度", "created": 0, "pending": 0, "abnormal": 0}, {"name": "航空加油", "created": 0, "pending": 0, "abnormal": 0}, {"name": "清水加注", "created": 0, "pending": 0, "abnormal": 0}, {"name": "排污作业", "created": 0, "pending": 0, "abnormal": 0}, {"name": "航食配餐", "created": 0, "pending": 0, "abnormal": 0}, {"name": "除冰除雪", "created": 0, "pending": 0, "abnormal": 0}, {"name": "推车作业", "created": 0, "pending": 0, "abnormal": 0}, {"name": "地面电源", "created": 0, "pending": 0, "abnormal": 0}, {"name": "空调车调度", "created": 0, "pending": 0, "abnormal": 0}, {"name": "机坪巡检", "created": 0, "pending": 0, "abnormal": 0}, {"name": "外来物排查", "created": 0, "pending": 0, "abnormal": 0}, {"name": "登机口分配", "created": 0, "pending": 0, "abnormal": 0}, {"name": "地勤人员", "created": 0, "pending": 0, "abnormal": 0}, {"name": "地勤设备", "created": 0, "pending": 0, "abnormal": 0}]
  }
})
</script>
