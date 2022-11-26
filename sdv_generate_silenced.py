from functools import partialmethod

from tqdm import tqdm


def sdv_generate_sample_silenced(model, seq_len):
    tqdm.__init__ = partialmethod(tqdm.__init__, disable=True)
    generated_sample = model.sample(sequence_length=seq_len)
    return generated_sample
