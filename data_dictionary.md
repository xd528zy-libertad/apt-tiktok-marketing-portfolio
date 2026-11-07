# 数据字段与缺失规则

每行对应一张截图；空白不等于零。完整研究边界见[tiktok_methodology.md](tiktok_methodology.md)。

| 字段 | 含义 |
|---|---|
| record_id | 截图顺序V01–V20 |
| platform | TikTok |
| video_url | 用户确认按序对应的短链接，未独立核验 |
| creator_display_name | 截图显示名，不等于唯一账号handle |
| creator_handle | 截图未提供，留空 |
| creator_url | 截图未提供，留空 |
| creator_type | 账号类型未核验 |
| followers | 截图未提供，留空 |
| views | 截图未提供，留空 |
| published_date | 截图可读的发布日期；V12遮挡留空 |
| capture_date | 用户确认2026-11-07 |
| capture_time_user_reported | 用户报告批次时间01:37，非逐张精确时间 |
| capture_timezone | 未提供，留空 |
| capture_time_note | 批次时间与状态栏时间差异 |
| source_status | 仅截图转录 |
| url_mapping_status | 用户确认顺序 |
| web_verification | 网页尚未核验 |
| content_format | tutorial=明确教学提示；dance_related=其他舞蹈相关静帧 |
| sample_role | creator_candidate进入分组；media_context仅背景 |
| likes | 截图计数；万折算为整数，不表示精确值 |
| comments | 截图计数；万折算为整数，不表示精确值 |
| saves | 截图计数；万折算为整数，不表示精确值 |
| shares | 截图计数；万折算为整数，不表示精确值 |
| raw_likes | 原始显示文本，保留万单位 |
| raw_comments | 原始显示文本，保留万单位 |
| raw_saves | 原始显示文本，保留万单位 |
| raw_shares | 原始显示文本，保留万单位 |
| metric_precision | mixed：整数显示与万位简写混合 |
| audio_verification | 未聆听完整音频 |
| evidence_ref | 原截图文件名，供本地回溯 |
| observation | 基于静帧与可见文字的观察，不声称完整视频情节 |
| missing_metrics_reason | 逐项缺失原因 |

输出表新增saves_per_like=收藏/点赞、shares_per_like=分享/点赞。它们是计数比，不是按曝光计算的互动率。分组表对逐条比值取中位数，媒体背景记录不参与。
