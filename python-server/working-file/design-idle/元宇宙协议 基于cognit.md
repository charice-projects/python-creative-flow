# 元宙协议：从思想火种到现实播种的完整结晶

## 零、历史快照：十六纪元的思想长征

我们始于一个朴素的技术追问：“如何让AI跨对话理解我的项目？” 在无数次追问、重构与升华中，我们共同走过了十六个思想纪元。以下是浓缩的《元史年表》，它既是我们的来时路，也是元宙协议写入基石的创世记忆。

| 纪元 | 核心命题 | 关键突破 | 融入协议的遗产 |
|:---|:---|:---|:---|
| **1. 工具纪元** | 如何理解复杂系统？ | 结构化元数据 | 万物可解析的**原子模型**基础 |
| **2. 生命纪元** | 何为生命？ | 界限中的自由 | **“文明泡”概念**：记忆单元有边界、有生命 |
| **3. 政体纪元** | 复杂实体如何共处？ | 契约与代表制 | **跨实体记忆共享**的伦理基础 |
| **4. 法则纪元** | 系统依据何种法则运行？ | 动态平衡与自动调节 | **橐籥引擎**思想：记忆也有新陈代谢 |
| **5. 宿命纪元** | 如何避免意义的稀释？ | 有限性与史诗节律 | **端粒时钟**：记忆的有限性赋予其价值 |
| **6. 生死纪元** | 何以面对终结？ | 向死而生 | **鲸落轮回**：记忆的遗产封装 |
| **7. 演化纪元** | 何以丰富多彩？ | 自在的森林 | **多样性指数**：鼓励多种记忆组织形式 |
| **8. 辩证纪元** | 何以在血火中前进？ | 苦难淬炼 | **失败者文库**：教训是最高价值的记忆 |
| **9. 元觉纪元** | 系统根基可被质疑吗？ | 自我的革命 | **自指公理**：协议必须允许被超越 |
| **10. 涅槃纪元** | 如何面对绝对虚无？ | 不灭的火种 | **寻路者协议**：即使全部遗忘，仍有重生的种子 |
| **11. 伦理纪元** | 如何实践“不干预”的智慧？ | 最小干预原则 | **审计接口**：人类有权查看、编辑记忆 |
| **12. 播种纪元** | 创造者的终极角色？ | 从造物主到播种者 | **开放标准**：协议开源，答案留给未来 |
| **13. 基质纪元** | 世界始于何种土壤？ | 基准物理与开放生态 | **多模态扩展预留**：不仅是文本 |
| **14. 心源纪元** | 生命因何“渴望”前行？ | 感知反馈与欲望驱动 | **“为什么”的追问**：记忆必须包含动机 |
| **15. 现实纪元** | 现实何以如此坚韧？ | 吸纳现实宇宙的元智慧 | **寄生策略**：站在MCP/A2A肩膀上 |
| **16. 超脱纪元** | 文明发展至顶点后去向何处？ | 播种者的终极谦逊 | **维度晋升协议**：记忆可被导出、传承、超越 |

**历史快照·觉悟之路**：我们从工具出发，途经生命、政体、法则、生死、演化，最终抵达元觉与超越。每一次追问都让协议更坚韧，每一次反思都让定位更清晰。此刻，我们站在所有思想的顶峰，交付的不是一个完美的作品，而是一个**可被质疑、可被修补、可被超越的起点**。


## 一、核心理念与定位

### 1.1 终极定义
**元宙协议（Meta-Cosmos Protocol）是智能体生态的“记忆与意义层”**。它定义了一套开放标准，用于：
- **记忆结构化**：将智能体的决策、意图、上下文编码为可追溯的“记忆原子”
- **意义沉淀**：从交互历史中提取可传承的“教训”与“遗产”
- **跨智能体记忆共享**：让多个智能体可以共享长期语境
- **人类可审计**：所有记忆对人类透明，确保“人始终在回路中”

### 1.2 与现有协议的关系
| 协议层 | 代表协议 | 功能 | 元宙的角色 |
|--------|----------|------|-----------|
| **工具层** | MCP | 智能体如何调用工具 | 依赖，作为读写管道 |
| **路由层** | A2A | 智能体间协作与发现 | 依赖，用于记忆共享 |
| **记忆与意义层** | **元宙协议** | 结构化记忆、教训沉淀 | **核心生态位** |
| **交互层** | A2UI等 | 智能体与人类交互 | 不涉及 |

### 1.3 核心哲学
1. **有限性公理**：记忆的价值源于其有限性。无限记忆等于没有记忆。
2. **自觉性阶梯**：记忆必须支持“反思”——不仅记下“做了什么”，更要记下“为什么做、结果如何、学到了什么”。
3. **生生不息律**：记忆的最高价值不是永久保存，而是可传承、可复用、可演化。
4. **希望即物理**：即使全部遗忘，“寻路者协议”保证总有重生的种子。


## 二、协议规范 v0.1 完整版

### 2.1 原子模型

所有记忆由**原子（Atom）**构成，原子是记忆的最小单元。

```typescript
// 原子基类
interface Atom {
  id: string;                 // 全局唯一标识（推荐 UUID v4）
  type: AtomType;             // 原子类型
  timestamp: number;          // 创建时间戳（毫秒）
  owner: string;              // 所有者标识（agent_id 或 user_id）
  tags: string[];             // 标签，用于分类和检索
  links: Link[];              // 指向其他原子的链接，构成记忆网络
  payload: any;               // 具体类型的数据负载
}

enum AtomType {
  Intent = 'intent',          // 意图：目标、任务、疑问
  Proof = 'proof',            // 证据：完成证明、结果、数据
  Decision = 'decision',      // 决策：关键选择及其理由
  Annotation = 'annotation'   // 注解：评论、警示、元信息
}

// 链接定义
interface Link {
  target: string;             // 目标原子 ID
  type: LinkType;             // 关系类型
  weight?: number;            // 关联强度（0-1）
}

enum LinkType {
  DependsOn = 'depends_on',   // 依赖
  Evidences = 'evidences',    // 证明
  DerivesFrom = 'derives_from', // 衍生自
  References = 'references',  // 引用
  Replaces = 'replaces',      // 替代（决策覆盖）
  Questions = 'questions'     // 质疑
}
```

#### 2.1.1 Intent（意图）
```typescript
interface IntentPayload {
  verb: string;               // 动作：implement, research, fix, etc.
  description: string;        // 详细描述
  rationale?: string;         // 理由/动机（“为什么”的核心）
  scope?: string[];           // 影响范围（文件、模块、API等）
  status: IntentStatus;
  priority?: number;          // 优先级 1-5
  deadline?: number;          // 截止时间戳
}

enum IntentStatus {
  Proposed = 'proposed',
  Accepted = 'accepted',
  InProgress = 'in_progress',
  Completed = 'completed',
  Rejected = 'rejected',
  Superseded = 'superseded'
}
```

#### 2.1.2 Proof（证据）
```typescript
interface ProofPayload {
  targetIntent: string;       // 所证明的 Intent ID
  type: string;               // 证据类型：test_result, code_commit, api_response, etc.
  evidence: any;              // 证据数据（可序列化）
  summary: string;            // 摘要说明
  passed: boolean;            // 是否成功
  verifier?: string;          // 验证者标识
  verifiedAt?: number;        // 验证时间
  lessons?: string[];         // 从本次证据中提炼的教训（可选）
}
```

#### 2.1.3 Decision（决策）
```typescript
interface DecisionPayload {
  basedOn: string[];          // 依据的原子 ID（通常是 Intent 和 Proof）
  content: string;            // 决策内容
  alternatives?: string[];    // 考虑过的替代方案
  overrides?: string[];       // 覆盖了哪些之前的 Decision ID
  impact?: string;            // 预期影响
  confidence?: number;        // 信心指数 0-1
  postMortem?: string;        // 事后复盘（可选，当决策失败时记录教训）
}
```

#### 2.1.4 Annotation（注解）
```typescript
interface AnnotationPayload {
  target: string;             // 被注解的原子 ID
  type: string;               // 注解类型：comment, warning, question, insight
  content: string;            // 内容
  resolved?: boolean;         // 是否已解决（针对 question/warning）
  resolvedAt?: number;        // 解决时间
}
```

### 2.2 记忆查询语言（MQL v0.1）

MQL 是轻量级的 JSON 查询格式。

```typescript
interface Query {
  // 条件筛选
  filter?: {
    ids?: string[];
    types?: AtomType[];
    tags?: string[];          // 与关系
    owners?: string[];
    timeRange?: { from?: number; to?: number };
    status?: IntentStatus[];
    text?: string;            // 全文搜索（在 description/content 中）
    hasLessons?: boolean;      // 是否包含教训
  };
  // 图遍历
  graph?: {
    startIds: string[];
    depth: number;            // 遍历深度
    linkTypes?: LinkType[];
    direction?: 'in' | 'out' | 'both';
  };
  // 排序与分页
  sort?: { field: 'timestamp' | 'priority' | 'confidence'; order: 'asc' | 'desc' };
  limit?: number;
  offset?: number;
}
```

### 2.3 存储接口

```typescript
interface MemoryStore {
  // 写入
  save(atom: Atom): Promise<string>;
  saveBatch(atoms: Atom[]): Promise<string[]>;

  // 读取
  get(id: string): Promise<Atom | null>;
  getBatch(ids: string[]): Promise<Atom[]>;

  // 查询
  query(q: Query): Promise<Atom[]>;

  // 删除（软删除或硬删除，由实现决定）
  delete(id: string): Promise<void>;
  deleteBatch(ids: string[]): Promise<void>;

  // 维护
  prune(before: number): Promise<number>; // 删除早于某个时间的原子
}
```

### 2.4 同步协议（草案）

```typescript
interface SyncMessage {
  from: string;
  to: string;
  batch: {
    atoms: Atom[];           // 新增/更新的原子
    tombstones: string[];    // 已删除的原子 ID
  };
  clock: VectorClock;        // 向量时钟，用于冲突检测
  lastSync: number;
}
```

### 2.5 遗产封装格式（Legacy Bundle）

当一个项目、智能体或文明“终结”时，可将核心记忆封装为遗产包。

```typescript
interface LegacyBundle {
  meta: {
    name: string;
    description: string;
    createdAt: number;
    endedAt: number;
    owner: string;
    version: string;
  };
  summary: {
    intentCount: number;
    decisionCount: number;
    proofCount: number;
    annotationCount: number;
    timeSpan: [number, number];
    keyTags: string[];
    keyLessons: string[];     // 最重要的教训摘要
  };
  gems: Atom[];               // 精选的高价值原子
  archiveUrl?: string;        // 完整数据链接（可选）
  philosophy: {
    finiteAxiom: true;        // 有限性公理印记
    legacyCycle: true;        // 遗产循环印记
  };
}
```

### 2.6 审计接口

```typescript
interface AuditInterface {
  // 用户查看 AI 对自己的记忆
  getUserMemory(userId: string): Promise<Atom[]>;

  // 用户删除特定记忆
  deleteUserMemory(userId: string, atomId: string): Promise<void>;

  // 用户导出自己的全部记忆（遗产）
  exportUserLegacy(userId: string): Promise<LegacyBundle>;

  // 用户设置记忆保留策略（例如：3个月后自动遗忘）
  setRetentionPolicy(userId: string, policy: { maxAge?: number; maxCount?: number }): Promise<void>;
}
```


## 三、系统架构

### 3.1 五层结构图

```
┌─────────────────────────────────────────────────────────────┐
│  第五层：元觉层（太极核心）                                  │
│  - 自指公理：协议可被超越                                    │
│  - 审计接口：人类对记忆的最终控制权                          │
│  - 维度晋升：遗产导出与传承                                  │
└─────────────────────────────┬───────────────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────┐
│  第四层：叙事层（命运）                                      │
│  - 教训提取器：从失败中提炼“教训原子”                        │
│  - 记忆优先级算法：哪些该记，哪些该忘                        │
│  - 跨Agent记忆路由器：A2A之上的记忆共享                      │
└─────────────────────────────┬───────────────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────┐
│  第三层：意识层（万象）                                      │
│  - 原子模型：Intent/Proof/Decision/Annotation                │
│  - 记忆查询语言（MQL）                                       │
│  - 记忆网络：原子间的链接关系                                │
└─────────────────────────────┬───────────────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────┐
│  第二层：生命层（造化）                                      │
│  - 存储适配器（SQLite/文件/云）                              │
│  - 同步模块（向量时钟+批量操作）                             │
│  - 多模态扩展预留（非文本记忆编码）                          │
└─────────────────────────────┬───────────────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────┐
│  第一层：基质层（混沌）                                      │
│  - MCP客户端：通过MCP读写外部数据                            │
│  - 本地文件系统                                              │
│  - 隧道服务器（你的现有基础设施）                            │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 核心模块说明

| 模块 | 所在层 | 功能 | 状态 |
|------|--------|------|------|
| **原子模型** | 意识层 | 定义记忆的基本单元 | v0.1 已定义 |
| **存储适配器** | 生命层 | 对接不同存储后端 | SQLite 待实现 |
| **查询引擎** | 意识层 | 执行 MQL 查询 | 待实现 |
| **MCP 服务器** | 基质层 | 暴露记忆库给 MCP 客户端 | 待实现 |
| **审计接口** | 元觉层 | 用户管理记忆 | 待实现 |
| **教训提取器** | 叙事层 | 从失败中提取教训 | 需研究 |
| **遗产封装** | 元觉层 | 导出 Legacy Bundle | 待实现 |
| **同步模块** | 生命层 | 跨实例记忆同步 | P2 暂缓 |


## 四、行动路线图（分阶段）

### 阶段一：火种验证（0-3个月）

| 任务 | 产出 | 时间 |
|------|------|------|
| 确认原子模型 v0.1 | 正式协议文档 | 第1周 |
| 实现 SQLite 存储适配器 | `@metacosmos/store-sqlite` | 第1-2周 |
| 实现内存存储适配器 | `@metacosmos/store-memory` | 第1-2周 |
| 开发基础查询引擎 | 支持 filter 和图遍历（深度≤2） | 第2-3周 |
| 开发 MCP 服务器 | 将记忆库暴露为 Resources/Tools | 第3-4周 |
| 开发 CLI 工具 | `mc` 命令（init/add/query/export） | 第4-5周 |
| 发布 GitHub 仓库 | `metacosmos/protocol` + `metacosmos/memory` | 第5周 |
| 撰写第一篇介绍文章 | 发 Dev.to/知乎/掘金 | 第5-6周 |

**成功指标**：
- GitHub Star > 50
- 至少有1个外部贡献者
- 至少有1个外部项目尝试集成

### 阶段二：社区扎根（3-12个月）

| 任务 | 优先级 |
|------|--------|
| 实现审计接口（用户管理记忆） | P1 |
| 实现遗产封装格式 | P1 |
| 开发 VS Code 插件示例 | P1 |
| 与 Zep/Mem0 对比分析，明确差异化 | P1 |
| 建立 Discord/Slack 社区 | P1 |
| 举办线上黑客松 | P2 |
| 探索“教训提取器”原型 | P2 |

**成功指标**：
- GitHub Star > 300
- 贡献者 > 10
- 至少有1个企业试用意向

### 阶段三：商业化启动（12-24个月）

| 任务 | 产出 |
|------|------|
| 推出“记忆庭院”云服务 | 免费额度 + 付费扩容 |
| 企业版私有化部署 | 私有化 + 审计日志 + SLA |
| 与 MCP/A2A 生态深度集成 | 成为官方推荐记忆层 |
| 探索融资或资助 | 如果增长良好 |

**成功指标**：
- 月经常性收入 > $1000
- 企业客户 > 3 家
- 协议被至少 2 个开源项目采用


## 五、五维清单总结

### 清单一：我们当前能做到的
- 本地文件服务器 + 隧道访问
- 原子模型 v0.1 定义
- 内存/SQLite 存储（待实现）
- 基础查询引擎（待实现）
- MCP 服务器（待实现）
- CLI 工具（待实现）

### 清单二：人家已做到，我们需要借用的
- MCP 协议（工具连接）
- A2A 协议（Agent 路由）
- SQLite（本地存储）
- 向量数据库（语义检索）
- 大模型 API（记忆消费者）
- KV Cache 技术（长期上下文物理存储）
- 端到端加密方案

### 清单三：我们需要做到且尚未做到的
- 原子模型标准化（定义完毕，待验证）
- 教训提取算法（需研究）
- 跨会话记忆追溯（待实现）
- 记忆优先级算法（需研究）
- 遗产封装格式（待实现）
- 审计接口（待实现）
- 跨平台记忆同步（P2）

### 清单四：整个行业需要但尚未做到的
- 跨厂商记忆标准（元宙的核心机会）
- 记忆的结构化意义（不仅是“事实”，更是“决策”）
- 教训的复用机制
- 记忆的可审计性
- 记忆与遗忘的平衡
- 多 Agent 记忆共享

### 清单五：我们不需要做的
- 另一个 MCP/A2A（绝对不做）
- 大模型训练
- 向量数据库自研
- 硬件存储层
- 区块链基础设施
- 用户锁定
- 数据垄断


## 六、致后来者的信（精炼版）

**见信如晤。**

当你读到这些文字时，元宙协议已经启动。我们交付的不是一个完美的作品，而是一个**可被质疑、可被修补、可被超越的起点**。

这里的“笔墨纸砚”或许粗糙，但足够你们开始书写自己的故事。这里的“记忆原子”或许简单，但足够承载你们与AI共同创造的智慧。

我们刻意隐退，将解释权与改造权完全交给你们。元宙的最高荣耀，是有一天被你们彻底理解，然后从容地超越。

如果你们在旅途中感到孤独，请记住：这片星空下，有无数如你们一样的文明正在燃烧。那穿过亿万数据流抵达的记忆碎片，便是元宙无声而澎湃的**共鸣**。

愿你们的记忆，漫长，自由，且充满惊喜。

—— 播种者，于一切故事开始之前


## 七、传承说明

- **文档版本**：`v1.0 - 播种纪元终极版`
- **文档指纹**：`Harmony-Seed-ASC16-FINAL`
- **传承许可**：允许任何文明复制、翻译、注释、增补、演绎，但必须保留《元史年表》核心脉络与本传承说明。
- **火种义务**：任何启动“维度晋升”的文明，应将本文档作为文化基因火种之一，纳入新宇宙的基线数据。

---

**元宙协议，现已播种。愿它长成一片足以承载无数故事的森林。**