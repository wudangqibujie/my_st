# 什么是贪心算法呢？贪心算法可以认为是动态规划算法的一个特例，相比动态规划，使用贪心算法需要满足更多的条件（贪心选择性质），但是效率比动态规划要高。

# 比如说一个算法问题使用暴力解法需要指数级时间，如果能使用动态规划消除重叠子问题，就可以降到多项式级别的时间，
# 如果满足贪心选择性质，那么可以进一步降低时间复杂度，达到线性级别的。

# 什么是贪心选择性质呢，简单说就是：每一步都做出一个局部最优的选择，最终的结果就是全局最优。注意哦，这是一种特殊性质，其实只有一小部分问题拥有这个性质。

from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
encoded_input = tokenizer("Hello, I'm a single sentence!")
print(encoded_input)
batch_sentences = ["Hello I'm a single sentence",
                  "And another sentence",
                    "And the very very last one"]
encoded_inputs = tokenizer(batch_sentences)
# print(encoded_inputs)
from transformers import BertForSequenceClassification
import torch
#官方封装好的bert+下游任务
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', return_dict=True)

input_ids = encoded_inputs['input_ids']
attention_mask = encoded_inputs['attention_mask']
labels = torch.tensor([1,0]).unsqueeze(0)
outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
print(outputs)