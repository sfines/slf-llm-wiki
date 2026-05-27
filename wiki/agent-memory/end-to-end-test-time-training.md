# End-to-End Test-Time Training (TTT-E2E)

End-to-End Test-Time Training (TTT-E2E) formulates long-context language modeling as a problem of continual learning rather than a purely architectural challenge. 

## Mechanism
Instead of relying on self-attention to losslessly recall an entire massive context window, the model continues learning at test time via next-token prediction on the given context. This explicitly compresses the read context into the model's weights. 
- **Inner Loop:** Directly optimizes the next-token prediction loss at test time.
- **Outer Loop:** At training time, meta-learning prepares the model's initialization specifically for test-time training, optimizing the final loss after the TTT process.

This end-to-end alignment between training-time initialization and test-time gradient steps allows the model to process long context efficiently with constant inference latency.

## References
- [End-to-End Test-Time Training for Long Context](../../raw/ttt-long-context.md)
