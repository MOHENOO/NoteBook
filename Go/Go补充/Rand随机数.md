```shell
import rand
func Seed(seed int64)
```

Seed uses the provided seed value to initialize the default Source to a deterministic state.
If Seed is not called,
the generator behaves as if seeded by Seed(1).
Seed values that have the same remainder when divided by 2³¹-1 generate the same pseudo-random sequence.
Seed, unlike the Rand.Seed method, is safe for concurrent use.
