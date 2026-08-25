洛克王国宠物图标素材库

## 用途

这里保存可在本地知识笔记中引用的独立洛克王国宠物图片。每只宠物一个 WebP 文件，避免把整张图鉴或攻略长图放进笔记。

## 当前素材

- 迪莫：`pets/dimo.webp`
- 喵喵：`pets/miaomiao.webp`
- 火花：`pets/huohua.webp`
- 水蓝蓝：`pets/shuilanlan.webp`
- 水灵：`pets/shuiling.webp`
- 奇丽花：`pets/qilihua.webp`
- 雪影娃娃：`pets/xueyingwawa.webp`
- 圣羽翼王：`pets/shengyuyiwang.webp`
- 板板壳：`pets/banbanke.webp`
- 咔咔壳：`pets/kakake.webp`
- 冬羽雀：`pets/dongyuque.webp`
- 岚鸟：`pets/laniao.webp`
- 音速犬：`pets/yinsugou.webp`
- 嘟嘟锅：`pets/duduguo.webp`
- 幽冥眼：`pets/youmingyan.webp`
- 小星光：`pets/xiaoxingguang.webp`
- 咔咔鸟：`pets/kakaniao.webp`
- 彩蝶鲨：`pets/caidiesha.webp`
- 影狸：`pets/yingli.webp`
- 小怂猫：`pets/xiaosongmao.webp`
- 小狮鹫：`pets/xiaoshijiu.webp`
- 圆号鱼：`pets/yuanhaoyu.webp`
- 古钟蛇：`pets/guzhongshe.webp`
- 圣代甜甜：`pets/shengdaitiantian.webp`
- 地鼠：`pets/ditu.webp`
- 遁地鼠：`pets/dundishu.webp`
- 咕德帽帽：`pets/gudemao.webp`

完整来源和原始文件名见 `manifest.json`。

## 完整图鉴

目前已统一保存 689 个 WebP 文件，全部位于 `pets/`：其中 662 个是完整图鉴的唯一宠物条目，另外 27 个是方便引用的精选别名。随机抽取只读取 `pets-index.json` 中的 662 个唯一条目，避免同一宠物因别名重复出现。已清理只有深色背景和名称文字、没有宠物主体的占位图；带有真实宠物形象的普通版、异色版和特殊版本仍然保留。

随机抽取示例：

```bash
python3 scripts/pick_pet_icons.py --count 5
```

## 来源与限制

素材来自 [SiNoCM/roco-pokedex](https://github.com/SiNoCM/roco-pokedex) 的 `images/` 目录；该项目说明图片资源来自 BWiki，图片版权归洛克王国官方所有。本目录仅作为本地个人学习和笔记素材使用，不用于商业传播。公开发布前需要自行确认授权范围。

## Markdown 引用示例

```markdown
![喵喵](../assets/rock-kingdom/pets/NO.002_喵喵.webp)
```

完整图鉴中的文件引用示例：

```markdown
![宠物](../assets/rock-kingdom/pets/NO.002_喵喵.webp)
```
