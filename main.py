
import torch

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM




def summarize(url):
    tokenizer = AutoTokenizer.from_pretrained("nsi319/legal-led-base-16384")
    model = AutoModelForSeq2SeqLM.from_pretrained("nsi319/legal-led-base-16384")

    padding = "max_length"

    text=url
    input_tokenized = tokenizer.encode(text, return_tensors='pt', padding=padding, pad_to_max_length=True, max_length=6144,
                                   truncation=True)
    summary_ids = model.generate(input_tokenized,
                             num_beams=4,
                             no_repeat_ngram_size=3,
                             length_penalty=2,
                             min_length=350,
                             max_length=500)
    summary = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False)for g in summary_ids][0]
    return summary