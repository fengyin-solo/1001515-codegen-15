<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">机场地面服务保障平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向航班过站保障、行李分拣转运、廊桥客梯调度、加油加水排污、除冰除雪与机坪安全巡检的一体化机场地面保障管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "航班信息", path: "/flight" }, { label: "停机位分配", path: "/stand" }, { label: "行李转运", path: "/baggage" }, { label: "廊桥调度", path: "/bridge" }, { label: "客梯车调度", path: "/stairs" }, { label: "航空加油", path: "/refuel_aviation" }, { label: "清水加注", path: "/water" }, { label: "排污作业", path: "/lavatory" }, { label: "航食配餐", path: "/catering" }, { label: "除冰除雪", path: "/deicing" }, { label: "推车作业", path: "/pushback" }, { label: "地面电源", path: "/gpu" }, { label: "空调车调度", path: "/acu" }, { label: "机坪巡检", path: "/ramp" }, { label: "外来物排查", path: "/fodb" }, { label: "登机口分配", path: "/board_gate" }, { label: "地勤人员", path: "/crew_ground" }, { label: "地勤设备", path: "/equipment_ground" }]
</script>
