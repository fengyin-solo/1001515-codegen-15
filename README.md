# 机场地面服务保障平台

面向航班过站保障、行李分拣转运、廊桥客梯调度、加油加水排污、除冰除雪与机坪安全巡检的一体化机场地面保障管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 航班信息 | `flight` | 航班 | 航班号、航空公司、机型 |
| 停机位分配 | `stand` | 停机位 | 机位编号、机位类型、适用机型 |
| 行李转运 | `baggage` | 行李转运单 | 转运单号、航班号、行李类型 |
| 廊桥调度 | `bridge` | 廊桥 | 廊桥编号、对接机位、对接型号 |
| 客梯车调度 | `stairs` | 客梯车 | 车牌号、车辆型号、梯高上限 |
| 航空加油 | `refuel_aviation` | 加油作业单 | 加油单号、航班号、油料类型 |
| 清水加注 | `water` | 加注作业单 | 加注单号、航班号、加注量 |
| 排污作业 | `lavatory` | 排污作业单 | 排污单号、航班号、排污车编号 |
| 航食配餐 | `catering` | 配餐单 | 配餐单号、航班号、餐食类型 |
| 除冰除雪 | `deicing` | 除冰作业单 | 除冰单号、航班号、除冰液类型 |
| 推车作业 | `pushback` | 推车作业单 | 推车单号、航班号、拖车编号 |
| 地面电源 | `gpu` | 电源车 | 车辆编号、电源类型、额定功率 |
| 空调车调度 | `acu` | 空调车 | 车辆编号、制冷功率、制热功率 |
| 机坪巡检 | `ramp` | 巡检记录 | 巡检编号、巡检区域、巡检时段 |
| 外来物排查 | `fodb` | 外来物记录 | 排查编号、发现位置、物品类型 |
| 登机口分配 | `board_gate` | 登机口 | 登机口编号、所在航站楼、适用航班 |
| 地勤人员 | `crew_ground` | 地勤人员 | 员工编号、姓名、工种岗位 |
| 地勤设备 | `equipment_ground` | 地勤设备 | 设备编号、设备名称、设备类型 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
