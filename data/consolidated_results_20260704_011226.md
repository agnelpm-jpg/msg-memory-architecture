# Consolidated Simulation Results

Generated: 2026-07-04 01:12:26
Total Runs: 11

---

## Run 1: run_20260704_010358_hsin

### Base Results

```json
{
  "master_seed": 865576579,
  "per_instance_params": [
    {
      "seed": 1201342591,
      "n_topics": 23,
      "n_turns": 509,
      "embed_dim": 52,
      "edge_density": 0.397,
      "update_rate": 0.327,
      "query_rate": 0.193,
      "distractor_rate": 0.277
    },
    {
      "seed": 1573960155,
      "n_topics": 19,
      "n_turns": 370,
      "embed_dim": 26,
      "edge_density": 0.532,
      "update_rate": 0.273,
      "query_rate": 0.173,
      "distractor_rate": 0.425
    },
    {
      "seed": 1212652411,
      "n_topics": 27,
      "n_turns": 545,
      "embed_dim": 49,
      "edge_density": 0.403,
      "update_rate": 0.152,
      "query_rate": 0.294,
      "distractor_rate": 0.286
    },
    {
      "seed": 1609273200,
      "n_topics": 35,
      "n_turns": 420,
      "embed_dim": 62,
      "edge_density": 0.497,
      "update_rate": 0.121,
      "query_rate": 0.186,
      "distractor_rate": 0.416
    },
    {
      "seed": 151258364,
      "n_topics": 16,
      "n_turns": 580,
      "embed_dim": 33,
      "edge_density": 0.345,
      "update_rate": 0.169,
      "query_rate": 0.255,
      "distractor_rate": 0.394
    },
    {
      "seed": 1607088261,
      "n_topics": 28,
      "n_turns": 436,
      "embed_dim": 44,
      "edge_density": 0.355,
      "update_rate": 0.295,
      "query_rate": 0.253,
      "distractor_rate": 0.272
    },
    {
      "seed": 2027835111,
      "n_topics": 38,
      "n_turns": 477,
      "embed_dim": 34,
      "edge_density": 0.498,
      "update_rate": 0.126,
      "query_rate": 0.222,
      "distractor_rate": 0.23
    },
    {
      "seed": 1704477021,
      "n_topics": 19,
      "n_turns": 459,
      "embed_dim": 34,
      "edge_density": 0.429,
      "update_rate": 0.332,
      "query_rate": 0.21,
      "distractor_rate": 0.296
    },
    {
      "seed": 1968801103,
      "n_topics": 28,
      "n_turns": 539,
      "embed_dim": 64,
      "edge_density": 0.496,
      "update_rate": 0.123,
      "query_rate": 0.233,
      "distractor_rate": 0.366
    },
    {
      "seed": 377514626,
      "n_topics": 32,
      "n_turns": 431,
      "embed_dim": 31,
      "edge_density": 0.475,
      "update_rate": 0.249,
      "query_rate": 0.15,
      "distractor_rate": 0.328
    },
    {
      "seed": 1432175059,
      "n_topics": 28,
      "n_turns": 566,
      "embed_dim": 48,
      "edge_density": 0.29,
      "update_rate": 0.13,
      "query_rate": 0.219,
      "distractor_rate": 0.446
    },
    {
      "seed": 1830307524,
      "n_topics": 32,
      "n_turns": 493,
      "embed_dim": 58,
      "edge_density": 0.312,
      "update_rate": 0.265,
      "query_rate": 0.248,
      "distractor_rate": 0.393
    }
  ],
  "summary": {
    "full": {
      "avg_tokens_per_turn": 58912.9,
      "avg_total_tokens": 28830052.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 185.1,
      "avg_total_tokens": 91197.0,
      "avg_accuracy": 0.3102
    },
    "msg": {
      "avg_tokens_per_turn": 42.4,
      "avg_total_tokens": 21290.0,
      "avg_accuracy": 0.5487,
      "avg_cue_rate": 0.7322,
      "avg_false_cue_rate": 0.2541,
      "avg_cascade_events": 50.8,
      "avg_socratic_events": 1.1,
      "avg_archived": 3.7
    }
  }
}
```

### Sweep Results

```json
{
  "0.05": {
    "full": {
      "avg_tokens_per_turn": 56448.7,
      "avg_total_tokens": 26185302.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 205.2,
      "avg_total_tokens": 93930.0,
      "avg_accuracy": 0.4016
    },
    "msg": {
      "avg_tokens_per_turn": 50.6,
      "avg_total_tokens": 23614.0,
      "avg_accuracy": 0.624,
      "avg_cue_rate": 0.8268,
      "avg_false_cue_rate": 0.2425,
      "avg_cascade_events": 12.1,
      "avg_socratic_events": 0.5,
      "avg_archived": 0.2
    }
  },
  "0.1": {
    "full": {
      "avg_tokens_per_turn": 48705.7,
      "avg_total_tokens": 19807648.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 218.9,
      "avg_total_tokens": 85056.0,
      "avg_accuracy": 0.4252
    },
    "msg": {
      "avg_tokens_per_turn": 48.9,
      "avg_total_tokens": 18074.0,
      "avg_accuracy": 0.5418,
      "avg_cue_rate": 0.7339,
      "avg_false_cue_rate": 0.2605,
      "avg_cascade_events": 21.8,
      "avg_socratic_events": 0.6,
      "avg_archived": 0.7
    }
  },
  "0.15": {
    "full": {
      "avg_tokens_per_turn": 56304.8,
      "avg_total_tokens": 26181256.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 200.4,
      "avg_total_tokens": 87445.0,
      "avg_accuracy": 0.3543
    },
    "msg": {
      "avg_tokens_per_turn": 46.4,
      "avg_total_tokens": 20520.0,
      "avg_accuracy": 0.6063,
      "avg_cue_rate": 0.8162,
      "avg_false_cue_rate": 0.2585,
      "avg_cascade_events": 30.8,
      "avg_socratic_events": 1.3,
      "avg_archived": 0.6
    }
  },
  "0.2": {
    "full": {
      "avg_tokens_per_turn": 62331.8,
      "avg_total_tokens": 30755417.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 246.4,
      "avg_total_tokens": 118789.0,
      "avg_accuracy": 0.319
    },
    "msg": {
      "avg_tokens_per_turn": 51.6,
      "avg_total_tokens": 23778.0,
      "avg_accuracy": 0.5117,
      "avg_cue_rate": 0.6713,
      "avg_false_cue_rate": 0.2338,
      "avg_cascade_events": 47.4,
      "avg_socratic_events": 1.3,
      "avg_archived": 2.8
    }
  },
  "0.3": {
    "full": {
      "avg_tokens_per_turn": 48922.0,
      "avg_total_tokens": 21827714.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 158.7,
      "avg_total_tokens": 63901.0,
      "avg_accuracy": 0.2412
    },
    "msg": {
      "avg_tokens_per_turn": 34.9,
      "avg_total_tokens": 13513.0,
      "avg_accuracy": 0.4297,
      "avg_cue_rate": 0.5713,
      "avg_false_cue_rate": 0.2704,
      "avg_cascade_events": 60.6,
      "avg_socratic_events": 2.4,
      "avg_archived": 3.3
    }
  },
  "0.4": {
    "full": {
      "avg_tokens_per_turn": 50261.2,
      "avg_total_tokens": 20660132.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 182.3,
      "avg_total_tokens": 67201.0,
      "avg_accuracy": 0.0707
    },
    "msg": {
      "avg_tokens_per_turn": 32.0,
      "avg_total_tokens": 12803.0,
      "avg_accuracy": 0.3978,
      "avg_cue_rate": 0.4984,
      "avg_false_cue_rate": 0.2342,
      "avg_cascade_events": 16.1,
      "avg_socratic_events": 12.2,
      "avg_archived": 2.2
    }
  }
}
```

---

## Run 2: run_20260704_010457_pqkd

### Base Results

```json
{
  "master_seed": 1003439118,
  "per_instance_params": [
    {
      "seed": 400739999,
      "n_topics": 31,
      "n_turns": 354,
      "embed_dim": 34,
      "edge_density": 0.324,
      "update_rate": 0.105,
      "query_rate": 0.19,
      "distractor_rate": 0.313
    },
    {
      "seed": 931078688,
      "n_topics": 16,
      "n_turns": 498,
      "embed_dim": 28,
      "edge_density": 0.532,
      "update_rate": 0.275,
      "query_rate": 0.199,
      "distractor_rate": 0.38
    },
    {
      "seed": 281424308,
      "n_topics": 15,
      "n_turns": 250,
      "embed_dim": 24,
      "edge_density": 0.382,
      "update_rate": 0.146,
      "query_rate": 0.234,
      "distractor_rate": 0.343
    },
    {
      "seed": 1855271384,
      "n_topics": 33,
      "n_turns": 427,
      "embed_dim": 57,
      "edge_density": 0.517,
      "update_rate": 0.235,
      "query_rate": 0.26,
      "distractor_rate": 0.322
    },
    {
      "seed": 1968887743,
      "n_topics": 36,
      "n_turns": 366,
      "embed_dim": 38,
      "edge_density": 0.312,
      "update_rate": 0.257,
      "query_rate": 0.173,
      "distractor_rate": 0.339
    },
    {
      "seed": 839402385,
      "n_topics": 20,
      "n_turns": 487,
      "embed_dim": 61,
      "edge_density": 0.254,
      "update_rate": 0.177,
      "query_rate": 0.169,
      "distractor_rate": 0.339
    },
    {
      "seed": 1071162914,
      "n_topics": 17,
      "n_turns": 320,
      "embed_dim": 24,
      "edge_density": 0.342,
      "update_rate": 0.125,
      "query_rate": 0.223,
      "distractor_rate": 0.228
    },
    {
      "seed": 1923200693,
      "n_topics": 33,
      "n_turns": 358,
      "embed_dim": 57,
      "edge_density": 0.365,
      "update_rate": 0.3,
      "query_rate": 0.224,
      "distractor_rate": 0.27
    },
    {
      "seed": 290819252,
      "n_topics": 17,
      "n_turns": 395,
      "embed_dim": 54,
      "edge_density": 0.254,
      "update_rate": 0.235,
      "query_rate": 0.216,
      "distractor_rate": 0.444
    },
    {
      "seed": 1272591434,
      "n_topics": 32,
      "n_turns": 268,
      "embed_dim": 55,
      "edge_density": 0.285,
      "update_rate": 0.339,
      "query_rate": 0.187,
      "distractor_rate": 0.397
    },
    {
      "seed": 74270007,
      "n_topics": 33,
      "n_turns": 424,
      "embed_dim": 34,
      "edge_density": 0.254,
      "update_rate": 0.252,
      "query_rate": 0.23,
      "distractor_rate": 0.213
    },
    {
      "seed": 1271235830,
      "n_topics": 24,
      "n_turns": 259,
      "embed_dim": 36,
      "edge_density": 0.481,
      "update_rate": 0.104,
      "query_rate": 0.236,
      "distractor_rate": 0.372
    }
  ],
  "summary": {
    "full": {
      "avg_tokens_per_turn": 45153.8,
      "avg_total_tokens": 17481107.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 210.2,
      "avg_total_tokens": 75318.0,
      "avg_accuracy": 0.3575
    },
    "msg": {
      "avg_tokens_per_turn": 39.3,
      "avg_total_tokens": 13960.0,
      "avg_accuracy": 0.509,
      "avg_cue_rate": 0.6862,
      "avg_false_cue_rate": 0.2535,
      "avg_cascade_events": 32.6,
      "avg_socratic_events": 1.8,
      "avg_archived": 2.1
    }
  }
}
```

### Sweep Results

```json
{
  "0.05": {
    "full": {
      "avg_tokens_per_turn": 53029.8,
      "avg_total_tokens": 24426204.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 193.9,
      "avg_total_tokens": 83072.0,
      "avg_accuracy": 0.4423
    },
    "msg": {
      "avg_tokens_per_turn": 51.0,
      "avg_total_tokens": 21010.0,
      "avg_accuracy": 0.6479,
      "avg_cue_rate": 0.8546,
      "avg_false_cue_rate": 0.2452,
      "avg_cascade_events": 9.2,
      "avg_socratic_events": 0.2,
      "avg_archived": 0.4
    }
  },
  "0.1": {
    "full": {
      "avg_tokens_per_turn": 54455.3,
      "avg_total_tokens": 23343716.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 209.1,
      "avg_total_tokens": 80825.0,
      "avg_accuracy": 0.3699
    },
    "msg": {
      "avg_tokens_per_turn": 49.2,
      "avg_total_tokens": 19231.0,
      "avg_accuracy": 0.6277,
      "avg_cue_rate": 0.8092,
      "avg_false_cue_rate": 0.2231,
      "avg_cascade_events": 23.0,
      "avg_socratic_events": 0.8,
      "avg_archived": 0.5
    }
  },
  "0.15": {
    "full": {
      "avg_tokens_per_turn": 50695.0,
      "avg_total_tokens": 21500921.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 206.4,
      "avg_total_tokens": 83277.0,
      "avg_accuracy": 0.3845
    },
    "msg": {
      "avg_tokens_per_turn": 41.4,
      "avg_total_tokens": 17061.0,
      "avg_accuracy": 0.5469,
      "avg_cue_rate": 0.7054,
      "avg_false_cue_rate": 0.235,
      "avg_cascade_events": 32.2,
      "avg_socratic_events": 0.6,
      "avg_archived": 0.8
    }
  },
  "0.2": {
    "full": {
      "avg_tokens_per_turn": 52483.5,
      "avg_total_tokens": 23170736.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 209.6,
      "avg_total_tokens": 87163.0,
      "avg_accuracy": 0.2902
    },
    "msg": {
      "avg_tokens_per_turn": 43.6,
      "avg_total_tokens": 18592.0,
      "avg_accuracy": 0.559,
      "avg_cue_rate": 0.7467,
      "avg_false_cue_rate": 0.2609,
      "avg_cascade_events": 35.5,
      "avg_socratic_events": 0.8,
      "avg_archived": 2.4
    }
  },
  "0.3": {
    "full": {
      "avg_tokens_per_turn": 49155.8,
      "avg_total_tokens": 20560793.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 220.2,
      "avg_total_tokens": 85500.0,
      "avg_accuracy": 0.2044
    },
    "msg": {
      "avg_tokens_per_turn": 44.8,
      "avg_total_tokens": 17992.0,
      "avg_accuracy": 0.5294,
      "avg_cue_rate": 0.6811,
      "avg_false_cue_rate": 0.2098,
      "avg_cascade_events": 40.7,
      "avg_socratic_events": 1.9,
      "avg_archived": 2.5
    }
  },
  "0.4": {
    "full": {
      "avg_tokens_per_turn": 42965.9,
      "avg_total_tokens": 15929585.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 172.7,
      "avg_total_tokens": 60985.0,
      "avg_accuracy": 0.09
    },
    "msg": {
      "avg_tokens_per_turn": 38.5,
      "avg_total_tokens": 12523.0,
      "avg_accuracy": 0.4792,
      "avg_cue_rate": 0.5997,
      "avg_false_cue_rate": 0.173,
      "avg_cascade_events": 17.7,
      "avg_socratic_events": 3.9,
      "avg_archived": 1.8
    }
  }
}
```

---

## Run 3: run_20260704_010504_rmek

### Base Results

```json
{
  "master_seed": 1116670113,
  "per_instance_params": [
    {
      "seed": 223690962,
      "n_topics": 23,
      "n_turns": 262,
      "embed_dim": 60,
      "edge_density": 0.473,
      "update_rate": 0.108,
      "query_rate": 0.17,
      "distractor_rate": 0.252
    },
    {
      "seed": 1220646796,
      "n_topics": 28,
      "n_turns": 595,
      "embed_dim": 35,
      "edge_density": 0.335,
      "update_rate": 0.185,
      "query_rate": 0.262,
      "distractor_rate": 0.26
    },
    {
      "seed": 1609778283,
      "n_topics": 31,
      "n_turns": 568,
      "embed_dim": 39,
      "edge_density": 0.5,
      "update_rate": 0.283,
      "query_rate": 0.298,
      "distractor_rate": 0.421
    },
    {
      "seed": 33255043,
      "n_topics": 32,
      "n_turns": 323,
      "embed_dim": 42,
      "edge_density": 0.371,
      "update_rate": 0.111,
      "query_rate": 0.223,
      "distractor_rate": 0.354
    },
    {
      "seed": 1158034638,
      "n_topics": 15,
      "n_turns": 272,
      "embed_dim": 24,
      "edge_density": 0.513,
      "update_rate": 0.233,
      "query_rate": 0.244,
      "distractor_rate": 0.274
    },
    {
      "seed": 2115383743,
      "n_topics": 18,
      "n_turns": 357,
      "embed_dim": 50,
      "edge_density": 0.372,
      "update_rate": 0.131,
      "query_rate": 0.18,
      "distractor_rate": 0.371
    },
    {
      "seed": 885143926,
      "n_topics": 26,
      "n_turns": 579,
      "embed_dim": 39,
      "edge_density": 0.387,
      "update_rate": 0.174,
      "query_rate": 0.17,
      "distractor_rate": 0.395
    },
    {
      "seed": 231281217,
      "n_topics": 38,
      "n_turns": 425,
      "embed_dim": 54,
      "edge_density": 0.399,
      "update_rate": 0.306,
      "query_rate": 0.193,
      "distractor_rate": 0.291
    },
    {
      "seed": 628010027,
      "n_topics": 32,
      "n_turns": 573,
      "embed_dim": 51,
      "edge_density": 0.455,
      "update_rate": 0.088,
      "query_rate": 0.194,
      "distractor_rate": 0.425
    },
    {
      "seed": 1240449562,
      "n_topics": 39,
      "n_turns": 339,
      "embed_dim": 30,
      "edge_density": 0.495,
      "update_rate": 0.137,
      "query_rate": 0.23,
      "distractor_rate": 0.375
    },
    {
      "seed": 1871613709,
      "n_topics": 39,
      "n_turns": 464,
      "embed_dim": 41,
      "edge_density": 0.266,
      "update_rate": 0.224,
      "query_rate": 0.185,
      "distractor_rate": 0.291
    },
    {
      "seed": 116082386,
      "n_topics": 29,
      "n_turns": 463,
      "embed_dim": 46,
      "edge_density": 0.486,
      "update_rate": 0.183,
      "query_rate": 0.291,
      "distractor_rate": 0.34
    }
  ],
  "summary": {
    "full": {
      "avg_tokens_per_turn": 56023.9,
      "avg_total_tokens": 26020819.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 186.1,
      "avg_total_tokens": 83363.0,
      "avg_accuracy": 0.3416
    },
    "msg": {
      "avg_tokens_per_turn": 47.2,
      "avg_total_tokens": 20922.0,
      "avg_accuracy": 0.6107,
      "avg_cue_rate": 0.7796,
      "avg_false_cue_rate": 0.2181,
      "avg_cascade_events": 33.0,
      "avg_socratic_events": 0.7,
      "avg_archived": 1.7
    }
  }
}
```

### Sweep Results

```json
{
  "0.05": {
    "full": {
      "avg_tokens_per_turn": 58260.9,
      "avg_total_tokens": 26186941.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 225.6,
      "avg_total_tokens": 98471.0,
      "avg_accuracy": 0.3824
    },
    "msg": {
      "avg_tokens_per_turn": 53.0,
      "avg_total_tokens": 23278.0,
      "avg_accuracy": 0.6383,
      "avg_cue_rate": 0.8153,
      "avg_false_cue_rate": 0.2245,
      "avg_cascade_events": 13.5,
      "avg_socratic_events": 0.3,
      "avg_archived": 0.1
    }
  },
  "0.1": {
    "full": {
      "avg_tokens_per_turn": 59604.9,
      "avg_total_tokens": 27243365.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 191.6,
      "avg_total_tokens": 83399.0,
      "avg_accuracy": 0.3856
    },
    "msg": {
      "avg_tokens_per_turn": 46.1,
      "avg_total_tokens": 19876.0,
      "avg_accuracy": 0.6443,
      "avg_cue_rate": 0.8468,
      "avg_false_cue_rate": 0.2435,
      "avg_cascade_events": 25.0,
      "avg_socratic_events": 0.7,
      "avg_archived": 0.6
    }
  },
  "0.15": {
    "full": {
      "avg_tokens_per_turn": 53119.7,
      "avg_total_tokens": 23540934.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 183.0,
      "avg_total_tokens": 73176.0,
      "avg_accuracy": 0.3605
    },
    "msg": {
      "avg_tokens_per_turn": 40.9,
      "avg_total_tokens": 16530.0,
      "avg_accuracy": 0.5409,
      "avg_cue_rate": 0.7289,
      "avg_false_cue_rate": 0.2598,
      "avg_cascade_events": 36.4,
      "avg_socratic_events": 0.8,
      "avg_archived": 1.1
    }
  },
  "0.2": {
    "full": {
      "avg_tokens_per_turn": 49811.8,
      "avg_total_tokens": 20486655.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 174.9,
      "avg_total_tokens": 67080.0,
      "avg_accuracy": 0.3497
    },
    "msg": {
      "avg_tokens_per_turn": 40.9,
      "avg_total_tokens": 15638.0,
      "avg_accuracy": 0.5522,
      "avg_cue_rate": 0.7064,
      "avg_false_cue_rate": 0.217,
      "avg_cascade_events": 34.5,
      "avg_socratic_events": 0.8,
      "avg_archived": 1.0
    }
  },
  "0.3": {
    "full": {
      "avg_tokens_per_turn": 47250.9,
      "avg_total_tokens": 19468836.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 229.9,
      "avg_total_tokens": 89547.0,
      "avg_accuracy": 0.2151
    },
    "msg": {
      "avg_tokens_per_turn": 35.5,
      "avg_total_tokens": 13530.0,
      "avg_accuracy": 0.4214,
      "avg_cue_rate": 0.5468,
      "avg_false_cue_rate": 0.2194,
      "avg_cascade_events": 35.5,
      "avg_socratic_events": 1.6,
      "avg_archived": 2.5
    }
  },
  "0.4": {
    "full": {
      "avg_tokens_per_turn": 53588.0,
      "avg_total_tokens": 23398741.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 159.4,
      "avg_total_tokens": 65160.0,
      "avg_accuracy": 0.1207
    },
    "msg": {
      "avg_tokens_per_turn": 28.4,
      "avg_total_tokens": 11518.0,
      "avg_accuracy": 0.3443,
      "avg_cue_rate": 0.4599,
      "avg_false_cue_rate": 0.3084,
      "avg_cascade_events": 33.8,
      "avg_socratic_events": 1.5,
      "avg_archived": 4.7
    }
  }
}
```

---

## Run 4: run_20260704_010512_gcbx

### Base Results

```json
{
  "master_seed": 3188866900,
  "per_instance_params": [
    {
      "seed": 53540973,
      "n_topics": 26,
      "n_turns": 397,
      "embed_dim": 47,
      "edge_density": 0.325,
      "update_rate": 0.163,
      "query_rate": 0.279,
      "distractor_rate": 0.341
    },
    {
      "seed": 1425786129,
      "n_topics": 22,
      "n_turns": 591,
      "embed_dim": 43,
      "edge_density": 0.546,
      "update_rate": 0.098,
      "query_rate": 0.28,
      "distractor_rate": 0.338
    },
    {
      "seed": 438145906,
      "n_topics": 19,
      "n_turns": 515,
      "embed_dim": 44,
      "edge_density": 0.53,
      "update_rate": 0.234,
      "query_rate": 0.225,
      "distractor_rate": 0.397
    },
    {
      "seed": 1996017718,
      "n_topics": 34,
      "n_turns": 508,
      "embed_dim": 25,
      "edge_density": 0.278,
      "update_rate": 0.305,
      "query_rate": 0.25,
      "distractor_rate": 0.372
    },
    {
      "seed": 1893264616,
      "n_topics": 31,
      "n_turns": 578,
      "embed_dim": 30,
      "edge_density": 0.393,
      "update_rate": 0.345,
      "query_rate": 0.198,
      "distractor_rate": 0.287
    },
    {
      "seed": 1333851999,
      "n_topics": 22,
      "n_turns": 486,
      "embed_dim": 61,
      "edge_density": 0.414,
      "update_rate": 0.196,
      "query_rate": 0.245,
      "distractor_rate": 0.371
    },
    {
      "seed": 329186534,
      "n_topics": 34,
      "n_turns": 547,
      "embed_dim": 53,
      "edge_density": 0.442,
      "update_rate": 0.208,
      "query_rate": 0.229,
      "distractor_rate": 0.358
    },
    {
      "seed": 822723931,
      "n_topics": 34,
      "n_turns": 573,
      "embed_dim": 29,
      "edge_density": 0.412,
      "update_rate": 0.138,
      "query_rate": 0.188,
      "distractor_rate": 0.441
    },
    {
      "seed": 1095811467,
      "n_topics": 39,
      "n_turns": 331,
      "embed_dim": 43,
      "edge_density": 0.537,
      "update_rate": 0.206,
      "query_rate": 0.279,
      "distractor_rate": 0.35
    },
    {
      "seed": 708720716,
      "n_topics": 18,
      "n_turns": 583,
      "embed_dim": 55,
      "edge_density": 0.43,
      "update_rate": 0.085,
      "query_rate": 0.158,
      "distractor_rate": 0.405
    },
    {
      "seed": 1562881493,
      "n_topics": 34,
      "n_turns": 368,
      "embed_dim": 31,
      "edge_density": 0.492,
      "update_rate": 0.236,
      "query_rate": 0.234,
      "distractor_rate": 0.324
    },
    {
      "seed": 460613045,
      "n_topics": 18,
      "n_turns": 313,
      "embed_dim": 30,
      "edge_density": 0.406,
      "update_rate": 0.326,
      "query_rate": 0.206,
      "distractor_rate": 0.356
    }
  ],
  "summary": {
    "full": {
      "avg_tokens_per_turn": 60619.3,
      "avg_total_tokens": 30593206.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 213.9,
      "avg_total_tokens": 98463.0,
      "avg_accuracy": 0.316
    },
    "msg": {
      "avg_tokens_per_turn": 41.2,
      "avg_total_tokens": 19591.0,
      "avg_accuracy": 0.5395,
      "avg_cue_rate": 0.7432,
      "avg_false_cue_rate": 0.2692,
      "avg_cascade_events": 42.8,
      "avg_socratic_events": 2.0,
      "avg_archived": 3.6
    }
  }
}
```

### Sweep Results

```json
{
  "0.05": {
    "full": {
      "avg_tokens_per_turn": 54428.4,
      "avg_total_tokens": 24958872.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 179.1,
      "avg_total_tokens": 79197.0,
      "avg_accuracy": 0.4256
    },
    "msg": {
      "avg_tokens_per_turn": 44.4,
      "avg_total_tokens": 19369.0,
      "avg_accuracy": 0.5823,
      "avg_cue_rate": 0.7783,
      "avg_false_cue_rate": 0.2509,
      "avg_cascade_events": 11.9,
      "avg_socratic_events": 0.2,
      "avg_archived": 0.2
    }
  },
  "0.1": {
    "full": {
      "avg_tokens_per_turn": 46843.8,
      "avg_total_tokens": 17528658.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 231.8,
      "avg_total_tokens": 82999.0,
      "avg_accuracy": 0.4399
    },
    "msg": {
      "avg_tokens_per_turn": 51.9,
      "avg_total_tokens": 18260.0,
      "avg_accuracy": 0.5621,
      "avg_cue_rate": 0.7399,
      "avg_false_cue_rate": 0.2426,
      "avg_cascade_events": 20.2,
      "avg_socratic_events": 0.6,
      "avg_archived": 0.7
    }
  },
  "0.15": {
    "full": {
      "avg_tokens_per_turn": 49880.1,
      "avg_total_tokens": 21310113.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 226.5,
      "avg_total_tokens": 96616.0,
      "avg_accuracy": 0.3775
    },
    "msg": {
      "avg_tokens_per_turn": 46.9,
      "avg_total_tokens": 19446.0,
      "avg_accuracy": 0.5531,
      "avg_cue_rate": 0.7596,
      "avg_false_cue_rate": 0.2722,
      "avg_cascade_events": 35.8,
      "avg_socratic_events": 0.8,
      "avg_archived": 0.9
    }
  },
  "0.2": {
    "full": {
      "avg_tokens_per_turn": 52878.7,
      "avg_total_tokens": 23938162.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 200.9,
      "avg_total_tokens": 85865.0,
      "avg_accuracy": 0.3041
    },
    "msg": {
      "avg_tokens_per_turn": 34.7,
      "avg_total_tokens": 14208.0,
      "avg_accuracy": 0.4819,
      "avg_cue_rate": 0.6343,
      "avg_false_cue_rate": 0.2468,
      "avg_cascade_events": 43.8,
      "avg_socratic_events": 1.6,
      "avg_archived": 1.9
    }
  },
  "0.3": {
    "full": {
      "avg_tokens_per_turn": 49728.3,
      "avg_total_tokens": 20383149.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 159.2,
      "avg_total_tokens": 62210.0,
      "avg_accuracy": 0.2492
    },
    "msg": {
      "avg_tokens_per_turn": 34.8,
      "avg_total_tokens": 13595.0,
      "avg_accuracy": 0.4472,
      "avg_cue_rate": 0.5964,
      "avg_false_cue_rate": 0.246,
      "avg_cascade_events": 58.0,
      "avg_socratic_events": 2.8,
      "avg_archived": 2.2
    }
  },
  "0.4": {
    "full": {
      "avg_tokens_per_turn": 53815.4,
      "avg_total_tokens": 24082446.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 196.1,
      "avg_total_tokens": 84501.0,
      "avg_accuracy": 0.0914
    },
    "msg": {
      "avg_tokens_per_turn": 37.7,
      "avg_total_tokens": 17109.0,
      "avg_accuracy": 0.4757,
      "avg_cue_rate": 0.5819,
      "avg_false_cue_rate": 0.1944,
      "avg_cascade_events": 43.4,
      "avg_socratic_events": 1.8,
      "avg_archived": 6.7
    }
  }
}
```

---

## Run 5: run_20260704_010520_gkrx

### Base Results

```json
{
  "master_seed": 512109876,
  "per_instance_params": [
    {
      "seed": 1564602188,
      "n_topics": 32,
      "n_turns": 355,
      "embed_dim": 54,
      "edge_density": 0.423,
      "update_rate": 0.233,
      "query_rate": 0.231,
      "distractor_rate": 0.217
    },
    {
      "seed": 113496513,
      "n_topics": 29,
      "n_turns": 589,
      "embed_dim": 45,
      "edge_density": 0.427,
      "update_rate": 0.308,
      "query_rate": 0.285,
      "distractor_rate": 0.321
    },
    {
      "seed": 1505264826,
      "n_topics": 18,
      "n_turns": 273,
      "embed_dim": 31,
      "edge_density": 0.298,
      "update_rate": 0.278,
      "query_rate": 0.232,
      "distractor_rate": 0.425
    },
    {
      "seed": 1967296294,
      "n_topics": 29,
      "n_turns": 361,
      "embed_dim": 57,
      "edge_density": 0.549,
      "update_rate": 0.148,
      "query_rate": 0.25,
      "distractor_rate": 0.355
    },
    {
      "seed": 1880198248,
      "n_topics": 20,
      "n_turns": 460,
      "embed_dim": 35,
      "edge_density": 0.483,
      "update_rate": 0.187,
      "query_rate": 0.286,
      "distractor_rate": 0.264
    },
    {
      "seed": 1902402068,
      "n_topics": 19,
      "n_turns": 559,
      "embed_dim": 58,
      "edge_density": 0.483,
      "update_rate": 0.263,
      "query_rate": 0.221,
      "distractor_rate": 0.272
    },
    {
      "seed": 248303604,
      "n_topics": 28,
      "n_turns": 493,
      "embed_dim": 42,
      "edge_density": 0.544,
      "update_rate": 0.336,
      "query_rate": 0.216,
      "distractor_rate": 0.337
    },
    {
      "seed": 515182514,
      "n_topics": 17,
      "n_turns": 300,
      "embed_dim": 52,
      "edge_density": 0.388,
      "update_rate": 0.095,
      "query_rate": 0.25,
      "distractor_rate": 0.339
    },
    {
      "seed": 71115788,
      "n_topics": 24,
      "n_turns": 504,
      "embed_dim": 42,
      "edge_density": 0.323,
      "update_rate": 0.163,
      "query_rate": 0.212,
      "distractor_rate": 0.33
    },
    {
      "seed": 15193503,
      "n_topics": 17,
      "n_turns": 325,
      "embed_dim": 64,
      "edge_density": 0.445,
      "update_rate": 0.258,
      "query_rate": 0.237,
      "distractor_rate": 0.398
    },
    {
      "seed": 577419561,
      "n_topics": 40,
      "n_turns": 305,
      "embed_dim": 37,
      "edge_density": 0.255,
      "update_rate": 0.317,
      "query_rate": 0.176,
      "distractor_rate": 0.436
    },
    {
      "seed": 1358860257,
      "n_topics": 26,
      "n_turns": 261,
      "embed_dim": 43,
      "edge_density": 0.45,
      "update_rate": 0.332,
      "query_rate": 0.161,
      "distractor_rate": 0.294
    }
  ],
  "summary": {
    "full": {
      "avg_tokens_per_turn": 50903.0,
      "avg_total_tokens": 21824939.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 192.0,
      "avg_total_tokens": 77921.0,
      "avg_accuracy": 0.2955
    },
    "msg": {
      "avg_tokens_per_turn": 39.9,
      "avg_total_tokens": 16124.0,
      "avg_accuracy": 0.547,
      "avg_cue_rate": 0.698,
      "avg_false_cue_rate": 0.2222,
      "avg_cascade_events": 52.6,
      "avg_socratic_events": 1.2,
      "avg_archived": 4.4
    }
  }
}
```

### Sweep Results

```json
{
  "0.05": {
    "full": {
      "avg_tokens_per_turn": 55793.8,
      "avg_total_tokens": 25643485.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 203.2,
      "avg_total_tokens": 89403.0,
      "avg_accuracy": 0.451
    },
    "msg": {
      "avg_tokens_per_turn": 52.3,
      "avg_total_tokens": 22331.0,
      "avg_accuracy": 0.6377,
      "avg_cue_rate": 0.8122,
      "avg_false_cue_rate": 0.2232,
      "avg_cascade_events": 13.3,
      "avg_socratic_events": 0.7,
      "avg_archived": 0.8
    }
  },
  "0.1": {
    "full": {
      "avg_tokens_per_turn": 48315.6,
      "avg_total_tokens": 19874455.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 195.5,
      "avg_total_tokens": 71791.0,
      "avg_accuracy": 0.4134
    },
    "msg": {
      "avg_tokens_per_turn": 42.6,
      "avg_total_tokens": 16795.0,
      "avg_accuracy": 0.5329,
      "avg_cue_rate": 0.7107,
      "avg_false_cue_rate": 0.2652,
      "avg_cascade_events": 19.7,
      "avg_socratic_events": 0.9,
      "avg_archived": 0.8
    }
  },
  "0.15": {
    "full": {
      "avg_tokens_per_turn": 53890.5,
      "avg_total_tokens": 22914808.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 216.9,
      "avg_total_tokens": 89317.0,
      "avg_accuracy": 0.3731
    },
    "msg": {
      "avg_tokens_per_turn": 46.1,
      "avg_total_tokens": 17925.0,
      "avg_accuracy": 0.5935,
      "avg_cue_rate": 0.7697,
      "avg_false_cue_rate": 0.2363,
      "avg_cascade_events": 31.8,
      "avg_socratic_events": 1.1,
      "avg_archived": 1.6
    }
  },
  "0.2": {
    "full": {
      "avg_tokens_per_turn": 51667.7,
      "avg_total_tokens": 22708689.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 205.5,
      "avg_total_tokens": 86210.0,
      "avg_accuracy": 0.3201
    },
    "msg": {
      "avg_tokens_per_turn": 37.4,
      "avg_total_tokens": 15572.0,
      "avg_accuracy": 0.4771,
      "avg_cue_rate": 0.6433,
      "avg_false_cue_rate": 0.2721,
      "avg_cascade_events": 45.3,
      "avg_socratic_events": 1.6,
      "avg_archived": 2.3
    }
  },
  "0.3": {
    "full": {
      "avg_tokens_per_turn": 48045.6,
      "avg_total_tokens": 20460447.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 198.3,
      "avg_total_tokens": 83170.0,
      "avg_accuracy": 0.2447
    },
    "msg": {
      "avg_tokens_per_turn": 36.9,
      "avg_total_tokens": 14638.0,
      "avg_accuracy": 0.4306,
      "avg_cue_rate": 0.5538,
      "avg_false_cue_rate": 0.2243,
      "avg_cascade_events": 37.0,
      "avg_socratic_events": 2.1,
      "avg_archived": 3.3
    }
  },
  "0.4": {
    "full": {
      "avg_tokens_per_turn": 58480.6,
      "avg_total_tokens": 28401919.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 187.0,
      "avg_total_tokens": 85504.0,
      "avg_accuracy": 0.0821
    },
    "msg": {
      "avg_tokens_per_turn": 30.5,
      "avg_total_tokens": 13820.0,
      "avg_accuracy": 0.4192,
      "avg_cue_rate": 0.5267,
      "avg_false_cue_rate": 0.1738,
      "avg_cascade_events": 11.6,
      "avg_socratic_events": 0.0,
      "avg_archived": 1.0
    }
  }
}
```

---

## Run 6: run_20260704_010528_bgqx

### Base Results

```json
{
  "master_seed": 2965694878,
  "per_instance_params": [
    {
      "seed": 868024610,
      "n_topics": 17,
      "n_turns": 373,
      "embed_dim": 46,
      "edge_density": 0.526,
      "update_rate": 0.329,
      "query_rate": 0.252,
      "distractor_rate": 0.207
    },
    {
      "seed": 756399711,
      "n_topics": 29,
      "n_turns": 412,
      "embed_dim": 64,
      "edge_density": 0.549,
      "update_rate": 0.209,
      "query_rate": 0.197,
      "distractor_rate": 0.327
    },
    {
      "seed": 339419489,
      "n_topics": 24,
      "n_turns": 503,
      "embed_dim": 24,
      "edge_density": 0.259,
      "update_rate": 0.205,
      "query_rate": 0.229,
      "distractor_rate": 0.332
    },
    {
      "seed": 11995757,
      "n_topics": 19,
      "n_turns": 368,
      "embed_dim": 55,
      "edge_density": 0.381,
      "update_rate": 0.331,
      "query_rate": 0.287,
      "distractor_rate": 0.374
    },
    {
      "seed": 2123658645,
      "n_topics": 34,
      "n_turns": 413,
      "embed_dim": 51,
      "edge_density": 0.505,
      "update_rate": 0.162,
      "query_rate": 0.169,
      "distractor_rate": 0.36
    },
    {
      "seed": 1155423525,
      "n_topics": 19,
      "n_turns": 596,
      "embed_dim": 46,
      "edge_density": 0.416,
      "update_rate": 0.228,
      "query_rate": 0.245,
      "distractor_rate": 0.234
    },
    {
      "seed": 1494191108,
      "n_topics": 30,
      "n_turns": 280,
      "embed_dim": 48,
      "edge_density": 0.389,
      "update_rate": 0.143,
      "query_rate": 0.236,
      "distractor_rate": 0.256
    },
    {
      "seed": 1259362975,
      "n_topics": 40,
      "n_turns": 497,
      "embed_dim": 64,
      "edge_density": 0.549,
      "update_rate": 0.293,
      "query_rate": 0.266,
      "distractor_rate": 0.371
    },
    {
      "seed": 1248902709,
      "n_topics": 19,
      "n_turns": 345,
      "embed_dim": 60,
      "edge_density": 0.302,
      "update_rate": 0.154,
      "query_rate": 0.192,
      "distractor_rate": 0.249
    },
    {
      "seed": 2048882360,
      "n_topics": 22,
      "n_turns": 258,
      "embed_dim": 52,
      "edge_density": 0.395,
      "update_rate": 0.277,
      "query_rate": 0.187,
      "distractor_rate": 0.298
    },
    {
      "seed": 576442574,
      "n_topics": 23,
      "n_turns": 487,
      "embed_dim": 60,
      "edge_density": 0.277,
      "update_rate": 0.124,
      "query_rate": 0.204,
      "distractor_rate": 0.375
    },
    {
      "seed": 618170341,
      "n_topics": 18,
      "n_turns": 463,
      "embed_dim": 50,
      "edge_density": 0.293,
      "update_rate": 0.278,
      "query_rate": 0.199,
      "distractor_rate": 0.221
    }
  ],
  "summary": {
    "full": {
      "avg_tokens_per_turn": 51793.5,
      "avg_total_tokens": 22546830.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 191.9,
      "avg_total_tokens": 80639.0,
      "avg_accuracy": 0.2834
    },
    "msg": {
      "avg_tokens_per_turn": 33.4,
      "avg_total_tokens": 14380.0,
      "avg_accuracy": 0.4421,
      "avg_cue_rate": 0.5532,
      "avg_false_cue_rate": 0.2146,
      "avg_cascade_events": 43.2,
      "avg_socratic_events": 0.9,
      "avg_archived": 2.8
    }
  }
}
```

### Sweep Results

```json
{
  "0.05": {
    "full": {
      "avg_tokens_per_turn": 52974.6,
      "avg_total_tokens": 22767536.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 187.7,
      "avg_total_tokens": 74806.0,
      "avg_accuracy": 0.4547
    },
    "msg": {
      "avg_tokens_per_turn": 53.1,
      "avg_total_tokens": 20853.0,
      "avg_accuracy": 0.7014,
      "avg_cue_rate": 0.9129,
      "avg_false_cue_rate": 0.2324,
      "avg_cascade_events": 13.4,
      "avg_socratic_events": 0.2,
      "avg_archived": 1.1
    }
  },
  "0.1": {
    "full": {
      "avg_tokens_per_turn": 61702.4,
      "avg_total_tokens": 29866999.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 222.9,
      "avg_total_tokens": 98408.0,
      "avg_accuracy": 0.358
    },
    "msg": {
      "avg_tokens_per_turn": 55.2,
      "avg_total_tokens": 23137.0,
      "avg_accuracy": 0.5655,
      "avg_cue_rate": 0.7251,
      "avg_false_cue_rate": 0.232,
      "avg_cascade_events": 26.8,
      "avg_socratic_events": 1.0,
      "avg_archived": 0.8
    }
  },
  "0.15": {
    "full": {
      "avg_tokens_per_turn": 51344.7,
      "avg_total_tokens": 21644640.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 246.8,
      "avg_total_tokens": 98459.0,
      "avg_accuracy": 0.4347
    },
    "msg": {
      "avg_tokens_per_turn": 50.3,
      "avg_total_tokens": 19854.0,
      "avg_accuracy": 0.6094,
      "avg_cue_rate": 0.7832,
      "avg_false_cue_rate": 0.2215,
      "avg_cascade_events": 26.0,
      "avg_socratic_events": 0.9,
      "avg_archived": 0.6
    }
  },
  "0.2": {
    "full": {
      "avg_tokens_per_turn": 51707.0,
      "avg_total_tokens": 22025368.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 177.8,
      "avg_total_tokens": 68634.0,
      "avg_accuracy": 0.3222
    },
    "msg": {
      "avg_tokens_per_turn": 34.6,
      "avg_total_tokens": 12457.0,
      "avg_accuracy": 0.4601,
      "avg_cue_rate": 0.6259,
      "avg_false_cue_rate": 0.2764,
      "avg_cascade_events": 42.8,
      "avg_socratic_events": 1.2,
      "avg_archived": 1.8
    }
  },
  "0.3": {
    "full": {
      "avg_tokens_per_turn": 58204.5,
      "avg_total_tokens": 27699647.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 206.3,
      "avg_total_tokens": 94503.0,
      "avg_accuracy": 0.2224
    },
    "msg": {
      "avg_tokens_per_turn": 45.0,
      "avg_total_tokens": 20069.0,
      "avg_accuracy": 0.5423,
      "avg_cue_rate": 0.7136,
      "avg_false_cue_rate": 0.2404,
      "avg_cascade_events": 58.1,
      "avg_socratic_events": 3.2,
      "avg_archived": 3.7
    }
  },
  "0.4": {
    "full": {
      "avg_tokens_per_turn": 51450.2,
      "avg_total_tokens": 24186188.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 172.8,
      "avg_total_tokens": 76361.0,
      "avg_accuracy": 0.0884
    },
    "msg": {
      "avg_tokens_per_turn": 28.3,
      "avg_total_tokens": 12855.0,
      "avg_accuracy": 0.3802,
      "avg_cue_rate": 0.4757,
      "avg_false_cue_rate": 0.2309,
      "avg_cascade_events": 27.1,
      "avg_socratic_events": 0.8,
      "avg_archived": 3.4
    }
  }
}
```

---

## Run 7: run_20260704_010536_xiuj

### Base Results

```json
{
  "master_seed": 731770865,
  "per_instance_params": [
    {
      "seed": 1498500279,
      "n_topics": 26,
      "n_turns": 505,
      "embed_dim": 47,
      "edge_density": 0.296,
      "update_rate": 0.278,
      "query_rate": 0.198,
      "distractor_rate": 0.389
    },
    {
      "seed": 832316631,
      "n_topics": 24,
      "n_turns": 290,
      "embed_dim": 31,
      "edge_density": 0.373,
      "update_rate": 0.162,
      "query_rate": 0.213,
      "distractor_rate": 0.386
    },
    {
      "seed": 370628340,
      "n_topics": 36,
      "n_turns": 578,
      "embed_dim": 60,
      "edge_density": 0.456,
      "update_rate": 0.133,
      "query_rate": 0.174,
      "distractor_rate": 0.404
    },
    {
      "seed": 317338375,
      "n_topics": 33,
      "n_turns": 336,
      "embed_dim": 30,
      "edge_density": 0.443,
      "update_rate": 0.188,
      "query_rate": 0.187,
      "distractor_rate": 0.271
    },
    {
      "seed": 776538563,
      "n_topics": 29,
      "n_turns": 447,
      "embed_dim": 64,
      "edge_density": 0.354,
      "update_rate": 0.23,
      "query_rate": 0.251,
      "distractor_rate": 0.414
    },
    {
      "seed": 1644133880,
      "n_topics": 18,
      "n_turns": 259,
      "embed_dim": 61,
      "edge_density": 0.397,
      "update_rate": 0.117,
      "query_rate": 0.19,
      "distractor_rate": 0.332
    },
    {
      "seed": 535502227,
      "n_topics": 31,
      "n_turns": 397,
      "embed_dim": 44,
      "edge_density": 0.358,
      "update_rate": 0.141,
      "query_rate": 0.217,
      "distractor_rate": 0.234
    },
    {
      "seed": 1936982512,
      "n_topics": 35,
      "n_turns": 538,
      "embed_dim": 54,
      "edge_density": 0.304,
      "update_rate": 0.156,
      "query_rate": 0.153,
      "distractor_rate": 0.418
    },
    {
      "seed": 1031580162,
      "n_topics": 31,
      "n_turns": 492,
      "embed_dim": 59,
      "edge_density": 0.251,
      "update_rate": 0.337,
      "query_rate": 0.264,
      "distractor_rate": 0.233
    },
    {
      "seed": 1406063899,
      "n_topics": 25,
      "n_turns": 550,
      "embed_dim": 47,
      "edge_density": 0.423,
      "update_rate": 0.243,
      "query_rate": 0.295,
      "distractor_rate": 0.322
    },
    {
      "seed": 304440780,
      "n_topics": 20,
      "n_turns": 540,
      "embed_dim": 26,
      "edge_density": 0.408,
      "update_rate": 0.148,
      "query_rate": 0.296,
      "distractor_rate": 0.404
    },
    {
      "seed": 113812357,
      "n_topics": 19,
      "n_turns": 251,
      "embed_dim": 28,
      "edge_density": 0.275,
      "update_rate": 0.225,
      "query_rate": 0.22,
      "distractor_rate": 0.295
    }
  ],
  "summary": {
    "full": {
      "avg_tokens_per_turn": 55010.1,
      "avg_total_tokens": 25262063.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 178.4,
      "avg_total_tokens": 77953.0,
      "avg_accuracy": 0.2924
    },
    "msg": {
      "avg_tokens_per_turn": 39.1,
      "avg_total_tokens": 16815.0,
      "avg_accuracy": 0.56,
      "avg_cue_rate": 0.715,
      "avg_false_cue_rate": 0.215,
      "avg_cascade_events": 39.1,
      "avg_socratic_events": 1.9,
      "avg_archived": 3.1
    }
  }
}
```

### Sweep Results

```json
{
  "0.05": {
    "full": {
      "avg_tokens_per_turn": 54797.8,
      "avg_total_tokens": 24285433.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 210.2,
      "avg_total_tokens": 89077.0,
      "avg_accuracy": 0.443
    },
    "msg": {
      "avg_tokens_per_turn": 58.6,
      "avg_total_tokens": 26124.0,
      "avg_accuracy": 0.6467,
      "avg_cue_rate": 0.8668,
      "avg_false_cue_rate": 0.2531,
      "avg_cascade_events": 11.3,
      "avg_socratic_events": 0.3,
      "avg_archived": 0.3
    }
  },
  "0.1": {
    "full": {
      "avg_tokens_per_turn": 54524.6,
      "avg_total_tokens": 24794716.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 218.3,
      "avg_total_tokens": 97099.0,
      "avg_accuracy": 0.3707
    },
    "msg": {
      "avg_tokens_per_turn": 51.7,
      "avg_total_tokens": 22407.0,
      "avg_accuracy": 0.6208,
      "avg_cue_rate": 0.8137,
      "avg_false_cue_rate": 0.2402,
      "avg_cascade_events": 23.4,
      "avg_socratic_events": 1.2,
      "avg_archived": 0.8
    }
  },
  "0.15": {
    "full": {
      "avg_tokens_per_turn": 53216.7,
      "avg_total_tokens": 22928664.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 210.4,
      "avg_total_tokens": 83320.0,
      "avg_accuracy": 0.3551
    },
    "msg": {
      "avg_tokens_per_turn": 36.9,
      "avg_total_tokens": 15058.0,
      "avg_accuracy": 0.5375,
      "avg_cue_rate": 0.7518,
      "avg_false_cue_rate": 0.2834,
      "avg_cascade_events": 31.3,
      "avg_socratic_events": 1.1,
      "avg_archived": 1.4
    }
  },
  "0.2": {
    "full": {
      "avg_tokens_per_turn": 55500.8,
      "avg_total_tokens": 25401406.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 195.8,
      "avg_total_tokens": 83607.0,
      "avg_accuracy": 0.3262
    },
    "msg": {
      "avg_tokens_per_turn": 42.9,
      "avg_total_tokens": 18938.0,
      "avg_accuracy": 0.517,
      "avg_cue_rate": 0.6758,
      "avg_false_cue_rate": 0.2409,
      "avg_cascade_events": 46.3,
      "avg_socratic_events": 1.8,
      "avg_archived": 1.9
    }
  },
  "0.3": {
    "full": {
      "avg_tokens_per_turn": 52265.6,
      "avg_total_tokens": 23102243.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 217.8,
      "avg_total_tokens": 88962.0,
      "avg_accuracy": 0.2371
    },
    "msg": {
      "avg_tokens_per_turn": 40.4,
      "avg_total_tokens": 16420.0,
      "avg_accuracy": 0.4709,
      "avg_cue_rate": 0.637,
      "avg_false_cue_rate": 0.258,
      "avg_cascade_events": 65.2,
      "avg_socratic_events": 3.1,
      "avg_archived": 5.0
    }
  },
  "0.4": {
    "full": {
      "avg_tokens_per_turn": 53376.6,
      "avg_total_tokens": 23006528.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 172.4,
      "avg_total_tokens": 70150.0,
      "avg_accuracy": 0.1347
    },
    "msg": {
      "avg_tokens_per_turn": 36.7,
      "avg_total_tokens": 14274.0,
      "avg_accuracy": 0.4916,
      "avg_cue_rate": 0.6031,
      "avg_false_cue_rate": 0.2,
      "avg_cascade_events": 35.8,
      "avg_socratic_events": 5.3,
      "avg_archived": 4.0
    }
  }
}
```

---

## Run 8: run_20260704_010544_diaj

### Base Results

```json
{
  "master_seed": 1194801639,
  "per_instance_params": [
    {
      "seed": 1978772195,
      "n_topics": 17,
      "n_turns": 399,
      "embed_dim": 29,
      "edge_density": 0.362,
      "update_rate": 0.267,
      "query_rate": 0.157,
      "distractor_rate": 0.211
    },
    {
      "seed": 1166828637,
      "n_topics": 17,
      "n_turns": 331,
      "embed_dim": 42,
      "edge_density": 0.295,
      "update_rate": 0.152,
      "query_rate": 0.295,
      "distractor_rate": 0.281
    },
    {
      "seed": 863194159,
      "n_topics": 15,
      "n_turns": 474,
      "embed_dim": 50,
      "edge_density": 0.325,
      "update_rate": 0.137,
      "query_rate": 0.182,
      "distractor_rate": 0.393
    },
    {
      "seed": 108500225,
      "n_topics": 20,
      "n_turns": 560,
      "embed_dim": 30,
      "edge_density": 0.384,
      "update_rate": 0.312,
      "query_rate": 0.204,
      "distractor_rate": 0.318
    },
    {
      "seed": 1427761589,
      "n_topics": 40,
      "n_turns": 294,
      "embed_dim": 32,
      "edge_density": 0.475,
      "update_rate": 0.135,
      "query_rate": 0.287,
      "distractor_rate": 0.222
    },
    {
      "seed": 1754192116,
      "n_topics": 20,
      "n_turns": 412,
      "embed_dim": 43,
      "edge_density": 0.379,
      "update_rate": 0.093,
      "query_rate": 0.175,
      "distractor_rate": 0.444
    },
    {
      "seed": 531405197,
      "n_topics": 29,
      "n_turns": 519,
      "embed_dim": 62,
      "edge_density": 0.286,
      "update_rate": 0.092,
      "query_rate": 0.178,
      "distractor_rate": 0.414
    },
    {
      "seed": 1508632033,
      "n_topics": 35,
      "n_turns": 542,
      "embed_dim": 41,
      "edge_density": 0.459,
      "update_rate": 0.191,
      "query_rate": 0.163,
      "distractor_rate": 0.233
    },
    {
      "seed": 1257567633,
      "n_topics": 20,
      "n_turns": 318,
      "embed_dim": 56,
      "edge_density": 0.437,
      "update_rate": 0.107,
      "query_rate": 0.218,
      "distractor_rate": 0.355
    },
    {
      "seed": 1953585838,
      "n_topics": 39,
      "n_turns": 364,
      "embed_dim": 46,
      "edge_density": 0.535,
      "update_rate": 0.273,
      "query_rate": 0.257,
      "distractor_rate": 0.285
    },
    {
      "seed": 1073007546,
      "n_topics": 20,
      "n_turns": 306,
      "embed_dim": 39,
      "edge_density": 0.272,
      "update_rate": 0.158,
      "query_rate": 0.201,
      "distractor_rate": 0.448
    },
    {
      "seed": 1568090875,
      "n_topics": 16,
      "n_turns": 292,
      "embed_dim": 38,
      "edge_density": 0.27,
      "update_rate": 0.345,
      "query_rate": 0.276,
      "distractor_rate": 0.243
    }
  ],
  "summary": {
    "full": {
      "avg_tokens_per_turn": 51899.5,
      "avg_total_tokens": 22287814.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 178.3,
      "avg_total_tokens": 68000.0,
      "avg_accuracy": 0.3102
    },
    "msg": {
      "avg_tokens_per_turn": 44.2,
      "avg_total_tokens": 17116.0,
      "avg_accuracy": 0.5845,
      "avg_cue_rate": 0.7678,
      "avg_false_cue_rate": 0.2442,
      "avg_cascade_events": 34.4,
      "avg_socratic_events": 2.1,
      "avg_archived": 1.8
    }
  }
}
```

### Sweep Results

```json
{
  "0.05": {
    "full": {
      "avg_tokens_per_turn": 50131.6,
      "avg_total_tokens": 20490338.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 205.3,
      "avg_total_tokens": 82652.0,
      "avg_accuracy": 0.4335
    },
    "msg": {
      "avg_tokens_per_turn": 44.1,
      "avg_total_tokens": 17697.0,
      "avg_accuracy": 0.5841,
      "avg_cue_rate": 0.7662,
      "avg_false_cue_rate": 0.241,
      "avg_cascade_events": 9.2,
      "avg_socratic_events": 0.2,
      "avg_archived": 0.7
    }
  },
  "0.1": {
    "full": {
      "avg_tokens_per_turn": 50280.3,
      "avg_total_tokens": 21104628.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 203.6,
      "avg_total_tokens": 82346.0,
      "avg_accuracy": 0.4009
    },
    "msg": {
      "avg_tokens_per_turn": 45.4,
      "avg_total_tokens": 18081.0,
      "avg_accuracy": 0.5836,
      "avg_cue_rate": 0.7594,
      "avg_false_cue_rate": 0.226,
      "avg_cascade_events": 19.9,
      "avg_socratic_events": 0.8,
      "avg_archived": 0.8
    }
  },
  "0.15": {
    "full": {
      "avg_tokens_per_turn": 55914.7,
      "avg_total_tokens": 26198948.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 195.1,
      "avg_total_tokens": 89322.0,
      "avg_accuracy": 0.3458
    },
    "msg": {
      "avg_tokens_per_turn": 47.7,
      "avg_total_tokens": 22134.0,
      "avg_accuracy": 0.5826,
      "avg_cue_rate": 0.7709,
      "avg_false_cue_rate": 0.2425,
      "avg_cascade_events": 40.7,
      "avg_socratic_events": 2.0,
      "avg_archived": 1.9
    }
  },
  "0.2": {
    "full": {
      "avg_tokens_per_turn": 56735.5,
      "avg_total_tokens": 26628681.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 143.3,
      "avg_total_tokens": 60310.0,
      "avg_accuracy": 0.3218
    },
    "msg": {
      "avg_tokens_per_turn": 37.8,
      "avg_total_tokens": 15120.0,
      "avg_accuracy": 0.551,
      "avg_cue_rate": 0.7084,
      "avg_false_cue_rate": 0.224,
      "avg_cascade_events": 50.8,
      "avg_socratic_events": 2.0,
      "avg_archived": 2.7
    }
  },
  "0.3": {
    "full": {
      "avg_tokens_per_turn": 55477.1,
      "avg_total_tokens": 26667211.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 174.8,
      "avg_total_tokens": 75209.0,
      "avg_accuracy": 0.2486
    },
    "msg": {
      "avg_tokens_per_turn": 31.7,
      "avg_total_tokens": 13060.0,
      "avg_accuracy": 0.3749,
      "avg_cue_rate": 0.4956,
      "avg_false_cue_rate": 0.3464,
      "avg_cascade_events": 49.8,
      "avg_socratic_events": 1.7,
      "avg_archived": 4.5
    }
  },
  "0.4": {
    "full": {
      "avg_tokens_per_turn": 45701.5,
      "avg_total_tokens": 18278084.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 169.7,
      "avg_total_tokens": 63836.0,
      "avg_accuracy": 0.1393
    },
    "msg": {
      "avg_tokens_per_turn": 28.2,
      "avg_total_tokens": 10308.0,
      "avg_accuracy": 0.4388,
      "avg_cue_rate": 0.5558,
      "avg_false_cue_rate": 0.2343,
      "avg_cascade_events": 28.3,
      "avg_socratic_events": 1.3,
      "avg_archived": 3.3
    }
  }
}
```

---

## Run 9: run_20260704_010552_wgkk

### Base Results

```json
{
  "master_seed": 2709248313,
  "per_instance_params": [
    {
      "seed": 346881639,
      "n_topics": 27,
      "n_turns": 345,
      "embed_dim": 41,
      "edge_density": 0.497,
      "update_rate": 0.088,
      "query_rate": 0.232,
      "distractor_rate": 0.335
    },
    {
      "seed": 1652201063,
      "n_topics": 29,
      "n_turns": 376,
      "embed_dim": 29,
      "edge_density": 0.484,
      "update_rate": 0.312,
      "query_rate": 0.227,
      "distractor_rate": 0.38
    },
    {
      "seed": 212701715,
      "n_topics": 32,
      "n_turns": 564,
      "embed_dim": 29,
      "edge_density": 0.35,
      "update_rate": 0.263,
      "query_rate": 0.253,
      "distractor_rate": 0.29
    },
    {
      "seed": 2113240723,
      "n_topics": 18,
      "n_turns": 544,
      "embed_dim": 34,
      "edge_density": 0.299,
      "update_rate": 0.331,
      "query_rate": 0.242,
      "distractor_rate": 0.273
    },
    {
      "seed": 241941553,
      "n_topics": 34,
      "n_turns": 252,
      "embed_dim": 36,
      "edge_density": 0.435,
      "update_rate": 0.218,
      "query_rate": 0.259,
      "distractor_rate": 0.404
    },
    {
      "seed": 1642152539,
      "n_topics": 15,
      "n_turns": 401,
      "embed_dim": 51,
      "edge_density": 0.455,
      "update_rate": 0.124,
      "query_rate": 0.297,
      "distractor_rate": 0.362
    },
    {
      "seed": 1979607069,
      "n_topics": 17,
      "n_turns": 367,
      "embed_dim": 57,
      "edge_density": 0.362,
      "update_rate": 0.238,
      "query_rate": 0.218,
      "distractor_rate": 0.237
    },
    {
      "seed": 1485435457,
      "n_topics": 32,
      "n_turns": 481,
      "embed_dim": 42,
      "edge_density": 0.35,
      "update_rate": 0.229,
      "query_rate": 0.286,
      "distractor_rate": 0.265
    },
    {
      "seed": 509944869,
      "n_topics": 19,
      "n_turns": 578,
      "embed_dim": 42,
      "edge_density": 0.421,
      "update_rate": 0.287,
      "query_rate": 0.299,
      "distractor_rate": 0.399
    },
    {
      "seed": 92951552,
      "n_topics": 25,
      "n_turns": 595,
      "embed_dim": 38,
      "edge_density": 0.396,
      "update_rate": 0.272,
      "query_rate": 0.217,
      "distractor_rate": 0.32
    },
    {
      "seed": 374403827,
      "n_topics": 24,
      "n_turns": 263,
      "embed_dim": 55,
      "edge_density": 0.37,
      "update_rate": 0.095,
      "query_rate": 0.18,
      "distractor_rate": 0.213
    },
    {
      "seed": 68259185,
      "n_topics": 27,
      "n_turns": 481,
      "embed_dim": 63,
      "edge_density": 0.384,
      "update_rate": 0.206,
      "query_rate": 0.19,
      "distractor_rate": 0.407
    }
  ],
  "summary": {
    "full": {
      "avg_tokens_per_turn": 58323.3,
      "avg_total_tokens": 27237726.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 212.0,
      "avg_total_tokens": 96085.0,
      "avg_accuracy": 0.2677
    },
    "msg": {
      "avg_tokens_per_turn": 49.8,
      "avg_total_tokens": 21801.0,
      "avg_accuracy": 0.5281,
      "avg_cue_rate": 0.6983,
      "avg_false_cue_rate": 0.2511,
      "avg_cascade_events": 41.9,
      "avg_socratic_events": 1.2,
      "avg_archived": 2.4
    }
  }
}
```

### Sweep Results

```json
{
  "0.05": {
    "full": {
      "avg_tokens_per_turn": 52089.6,
      "avg_total_tokens": 22219846.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 197.0,
      "avg_total_tokens": 79419.0,
      "avg_accuracy": 0.4644
    },
    "msg": {
      "avg_tokens_per_turn": 49.7,
      "avg_total_tokens": 20033.0,
      "avg_accuracy": 0.6695,
      "avg_cue_rate": 0.8746,
      "avg_false_cue_rate": 0.2356,
      "avg_cascade_events": 14.2,
      "avg_socratic_events": 0.6,
      "avg_archived": 0.3
    }
  },
  "0.1": {
    "full": {
      "avg_tokens_per_turn": 56930.5,
      "avg_total_tokens": 26484435.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 203.2,
      "avg_total_tokens": 90566.0,
      "avg_accuracy": 0.3729
    },
    "msg": {
      "avg_tokens_per_turn": 48.3,
      "avg_total_tokens": 21415.0,
      "avg_accuracy": 0.6007,
      "avg_cue_rate": 0.7958,
      "avg_false_cue_rate": 0.249,
      "avg_cascade_events": 23.5,
      "avg_socratic_events": 1.3,
      "avg_archived": 1.1
    }
  },
  "0.15": {
    "full": {
      "avg_tokens_per_turn": 48957.2,
      "avg_total_tokens": 20505482.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 199.3,
      "avg_total_tokens": 80539.0,
      "avg_accuracy": 0.4075
    },
    "msg": {
      "avg_tokens_per_turn": 45.3,
      "avg_total_tokens": 18627.0,
      "avg_accuracy": 0.613,
      "avg_cue_rate": 0.8269,
      "avg_false_cue_rate": 0.2598,
      "avg_cascade_events": 32.4,
      "avg_socratic_events": 0.4,
      "avg_archived": 1.2
    }
  },
  "0.2": {
    "full": {
      "avg_tokens_per_turn": 54324.1,
      "avg_total_tokens": 23886296.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 219.1,
      "avg_total_tokens": 93756.0,
      "avg_accuracy": 0.3197
    },
    "msg": {
      "avg_tokens_per_turn": 42.2,
      "avg_total_tokens": 18221.0,
      "avg_accuracy": 0.565,
      "avg_cue_rate": 0.7416,
      "avg_false_cue_rate": 0.2442,
      "avg_cascade_events": 37.3,
      "avg_socratic_events": 1.3,
      "avg_archived": 2.8
    }
  },
  "0.3": {
    "full": {
      "avg_tokens_per_turn": 53059.2,
      "avg_total_tokens": 24008299.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 181.4,
      "avg_total_tokens": 79607.0,
      "avg_accuracy": 0.2203
    },
    "msg": {
      "avg_tokens_per_turn": 30.5,
      "avg_total_tokens": 12907.0,
      "avg_accuracy": 0.3995,
      "avg_cue_rate": 0.5299,
      "avg_false_cue_rate": 0.2477,
      "avg_cascade_events": 40.7,
      "avg_socratic_events": 6.2,
      "avg_archived": 3.4
    }
  },
  "0.4": {
    "full": {
      "avg_tokens_per_turn": 54400.9,
      "avg_total_tokens": 24224121.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 182.6,
      "avg_total_tokens": 77000.0,
      "avg_accuracy": 0.1263
    },
    "msg": {
      "avg_tokens_per_turn": 34.7,
      "avg_total_tokens": 13614.0,
      "avg_accuracy": 0.4363,
      "avg_cue_rate": 0.5584,
      "avg_false_cue_rate": 0.2448,
      "avg_cascade_events": 43.3,
      "avg_socratic_events": 2.2,
      "avg_archived": 4.9
    }
  }
}
```

---

## Run 10: run_20260704_010600_zlhi

### Base Results

```json
{
  "master_seed": 2721855413,
  "per_instance_params": [
    {
      "seed": 796012730,
      "n_topics": 22,
      "n_turns": 596,
      "embed_dim": 33,
      "edge_density": 0.417,
      "update_rate": 0.283,
      "query_rate": 0.232,
      "distractor_rate": 0.367
    },
    {
      "seed": 1112263628,
      "n_topics": 39,
      "n_turns": 332,
      "embed_dim": 56,
      "edge_density": 0.505,
      "update_rate": 0.231,
      "query_rate": 0.27,
      "distractor_rate": 0.366
    },
    {
      "seed": 1807834504,
      "n_topics": 31,
      "n_turns": 344,
      "embed_dim": 49,
      "edge_density": 0.519,
      "update_rate": 0.241,
      "query_rate": 0.29,
      "distractor_rate": 0.356
    },
    {
      "seed": 1397241832,
      "n_topics": 25,
      "n_turns": 559,
      "embed_dim": 32,
      "edge_density": 0.503,
      "update_rate": 0.262,
      "query_rate": 0.216,
      "distractor_rate": 0.345
    },
    {
      "seed": 33538517,
      "n_topics": 38,
      "n_turns": 449,
      "embed_dim": 27,
      "edge_density": 0.521,
      "update_rate": 0.155,
      "query_rate": 0.214,
      "distractor_rate": 0.387
    },
    {
      "seed": 979833326,
      "n_topics": 25,
      "n_turns": 259,
      "embed_dim": 30,
      "edge_density": 0.282,
      "update_rate": 0.168,
      "query_rate": 0.282,
      "distractor_rate": 0.332
    },
    {
      "seed": 145148572,
      "n_topics": 24,
      "n_turns": 336,
      "embed_dim": 53,
      "edge_density": 0.36,
      "update_rate": 0.1,
      "query_rate": 0.161,
      "distractor_rate": 0.24
    },
    {
      "seed": 1332725893,
      "n_topics": 18,
      "n_turns": 288,
      "embed_dim": 62,
      "edge_density": 0.493,
      "update_rate": 0.268,
      "query_rate": 0.217,
      "distractor_rate": 0.276
    },
    {
      "seed": 1452603063,
      "n_topics": 19,
      "n_turns": 429,
      "embed_dim": 36,
      "edge_density": 0.269,
      "update_rate": 0.302,
      "query_rate": 0.251,
      "distractor_rate": 0.382
    },
    {
      "seed": 260333121,
      "n_topics": 15,
      "n_turns": 503,
      "embed_dim": 28,
      "edge_density": 0.473,
      "update_rate": 0.195,
      "query_rate": 0.259,
      "distractor_rate": 0.412
    },
    {
      "seed": 1001728596,
      "n_topics": 34,
      "n_turns": 260,
      "embed_dim": 44,
      "edge_density": 0.48,
      "update_rate": 0.198,
      "query_rate": 0.294,
      "distractor_rate": 0.418
    },
    {
      "seed": 2118610507,
      "n_topics": 21,
      "n_turns": 356,
      "embed_dim": 64,
      "edge_density": 0.389,
      "update_rate": 0.288,
      "query_rate": 0.165,
      "distractor_rate": 0.241
    }
  ],
  "summary": {
    "full": {
      "avg_tokens_per_turn": 51459.9,
      "avg_total_tokens": 22167684.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 212.9,
      "avg_total_tokens": 83550.0,
      "avg_accuracy": 0.3081
    },
    "msg": {
      "avg_tokens_per_turn": 35.6,
      "avg_total_tokens": 14142.0,
      "avg_accuracy": 0.4418,
      "avg_cue_rate": 0.5965,
      "avg_false_cue_rate": 0.2787,
      "avg_cascade_events": 44.2,
      "avg_socratic_events": 1.5,
      "avg_archived": 3.5
    }
  }
}
```

### Sweep Results

```json
{
  "0.05": {
    "full": {
      "avg_tokens_per_turn": 54851.0,
      "avg_total_tokens": 24829214.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 179.6,
      "avg_total_tokens": 76962.0,
      "avg_accuracy": 0.4197
    },
    "msg": {
      "avg_tokens_per_turn": 43.2,
      "avg_total_tokens": 18453.0,
      "avg_accuracy": 0.6049,
      "avg_cue_rate": 0.7922,
      "avg_false_cue_rate": 0.2362,
      "avg_cascade_events": 12.8,
      "avg_socratic_events": 0.4,
      "avg_archived": 0.2
    }
  },
  "0.1": {
    "full": {
      "avg_tokens_per_turn": 57517.5,
      "avg_total_tokens": 27162832.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 236.0,
      "avg_total_tokens": 104295.0,
      "avg_accuracy": 0.4067
    },
    "msg": {
      "avg_tokens_per_turn": 55.7,
      "avg_total_tokens": 25244.0,
      "avg_accuracy": 0.6253,
      "avg_cue_rate": 0.8171,
      "avg_false_cue_rate": 0.2361,
      "avg_cascade_events": 22.5,
      "avg_socratic_events": 1.1,
      "avg_archived": 0.7
    }
  },
  "0.15": {
    "full": {
      "avg_tokens_per_turn": 54710.2,
      "avg_total_tokens": 24462003.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 231.9,
      "avg_total_tokens": 96818.0,
      "avg_accuracy": 0.3839
    },
    "msg": {
      "avg_tokens_per_turn": 49.8,
      "avg_total_tokens": 20758.0,
      "avg_accuracy": 0.5889,
      "avg_cue_rate": 0.7917,
      "avg_false_cue_rate": 0.255,
      "avg_cascade_events": 28.7,
      "avg_socratic_events": 0.5,
      "avg_archived": 1.9
    }
  },
  "0.2": {
    "full": {
      "avg_tokens_per_turn": 59712.0,
      "avg_total_tokens": 29501503.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 196.3,
      "avg_total_tokens": 95073.0,
      "avg_accuracy": 0.2641
    },
    "msg": {
      "avg_tokens_per_turn": 38.6,
      "avg_total_tokens": 18342.0,
      "avg_accuracy": 0.4806,
      "avg_cue_rate": 0.6561,
      "avg_false_cue_rate": 0.2715,
      "avg_cascade_events": 44.1,
      "avg_socratic_events": 1.8,
      "avg_archived": 2.2
    }
  },
  "0.3": {
    "full": {
      "avg_tokens_per_turn": 53757.6,
      "avg_total_tokens": 24980012.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 168.6,
      "avg_total_tokens": 74970.0,
      "avg_accuracy": 0.2064
    },
    "msg": {
      "avg_tokens_per_turn": 36.0,
      "avg_total_tokens": 15980.0,
      "avg_accuracy": 0.4255,
      "avg_cue_rate": 0.5745,
      "avg_false_cue_rate": 0.2647,
      "avg_cascade_events": 54.8,
      "avg_socratic_events": 3.0,
      "avg_archived": 4.0
    }
  },
  "0.4": {
    "full": {
      "avg_tokens_per_turn": 51032.4,
      "avg_total_tokens": 22075554.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 163.0,
      "avg_total_tokens": 65149.0,
      "avg_accuracy": 0.1429
    },
    "msg": {
      "avg_tokens_per_turn": 20.0,
      "avg_total_tokens": 8056.0,
      "avg_accuracy": 0.2546,
      "avg_cue_rate": 0.3365,
      "avg_false_cue_rate": 0.1756,
      "avg_cascade_events": 42.2,
      "avg_socratic_events": 2.3,
      "avg_archived": 5.2
    }
  }
}
```

---

## Run 11: run_20260704_010608_fihj

### Base Results

```json
{
  "master_seed": 1960429129,
  "per_instance_params": [
    {
      "seed": 289914679,
      "n_topics": 21,
      "n_turns": 341,
      "embed_dim": 36,
      "edge_density": 0.405,
      "update_rate": 0.231,
      "query_rate": 0.181,
      "distractor_rate": 0.294
    },
    {
      "seed": 2056294957,
      "n_topics": 34,
      "n_turns": 433,
      "embed_dim": 55,
      "edge_density": 0.538,
      "update_rate": 0.21,
      "query_rate": 0.169,
      "distractor_rate": 0.428
    },
    {
      "seed": 1187838653,
      "n_topics": 24,
      "n_turns": 546,
      "embed_dim": 45,
      "edge_density": 0.441,
      "update_rate": 0.273,
      "query_rate": 0.227,
      "distractor_rate": 0.392
    },
    {
      "seed": 312977071,
      "n_topics": 16,
      "n_turns": 570,
      "embed_dim": 57,
      "edge_density": 0.459,
      "update_rate": 0.292,
      "query_rate": 0.292,
      "distractor_rate": 0.43
    },
    {
      "seed": 392512908,
      "n_topics": 20,
      "n_turns": 522,
      "embed_dim": 59,
      "edge_density": 0.359,
      "update_rate": 0.283,
      "query_rate": 0.299,
      "distractor_rate": 0.41
    },
    {
      "seed": 476605819,
      "n_topics": 18,
      "n_turns": 401,
      "embed_dim": 53,
      "edge_density": 0.459,
      "update_rate": 0.195,
      "query_rate": 0.215,
      "distractor_rate": 0.248
    },
    {
      "seed": 408732001,
      "n_topics": 17,
      "n_turns": 447,
      "embed_dim": 59,
      "edge_density": 0.447,
      "update_rate": 0.152,
      "query_rate": 0.156,
      "distractor_rate": 0.246
    },
    {
      "seed": 408737457,
      "n_topics": 34,
      "n_turns": 542,
      "embed_dim": 53,
      "edge_density": 0.376,
      "update_rate": 0.288,
      "query_rate": 0.296,
      "distractor_rate": 0.327
    },
    {
      "seed": 924267944,
      "n_topics": 19,
      "n_turns": 540,
      "embed_dim": 40,
      "edge_density": 0.383,
      "update_rate": 0.222,
      "query_rate": 0.179,
      "distractor_rate": 0.229
    },
    {
      "seed": 142925048,
      "n_topics": 33,
      "n_turns": 547,
      "embed_dim": 27,
      "edge_density": 0.335,
      "update_rate": 0.32,
      "query_rate": 0.184,
      "distractor_rate": 0.272
    },
    {
      "seed": 762270943,
      "n_topics": 38,
      "n_turns": 383,
      "embed_dim": 28,
      "edge_density": 0.527,
      "update_rate": 0.108,
      "query_rate": 0.193,
      "distractor_rate": 0.31
    },
    {
      "seed": 1700066528,
      "n_topics": 33,
      "n_turns": 473,
      "embed_dim": 59,
      "edge_density": 0.303,
      "update_rate": 0.154,
      "query_rate": 0.289,
      "distractor_rate": 0.417
    }
  ],
  "summary": {
    "full": {
      "avg_tokens_per_turn": 61991.1,
      "avg_total_tokens": 30186067.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 178.5,
      "avg_total_tokens": 84715.0,
      "avg_accuracy": 0.2477
    },
    "msg": {
      "avg_tokens_per_turn": 41.7,
      "avg_total_tokens": 19724.0,
      "avg_accuracy": 0.5249,
      "avg_cue_rate": 0.6646,
      "avg_false_cue_rate": 0.2091,
      "avg_cascade_events": 43.7,
      "avg_socratic_events": 2.2,
      "avg_archived": 3.5
    }
  }
}
```

### Sweep Results

```json
{
  "0.05": {
    "full": {
      "avg_tokens_per_turn": 58940.1,
      "avg_total_tokens": 28655658.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 176.8,
      "avg_total_tokens": 81149.0,
      "avg_accuracy": 0.3883
    },
    "msg": {
      "avg_tokens_per_turn": 47.1,
      "avg_total_tokens": 21527.0,
      "avg_accuracy": 0.6114,
      "avg_cue_rate": 0.8327,
      "avg_false_cue_rate": 0.2672,
      "avg_cascade_events": 18.2,
      "avg_socratic_events": 0.3,
      "avg_archived": 0.4
    }
  },
  "0.1": {
    "full": {
      "avg_tokens_per_turn": 55036.8,
      "avg_total_tokens": 25110193.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 196.6,
      "avg_total_tokens": 87337.0,
      "avg_accuracy": 0.4255
    },
    "msg": {
      "avg_tokens_per_turn": 43.9,
      "avg_total_tokens": 19055.0,
      "avg_accuracy": 0.59,
      "avg_cue_rate": 0.8015,
      "avg_false_cue_rate": 0.2648,
      "avg_cascade_events": 17.8,
      "avg_socratic_events": 0.7,
      "avg_archived": 0.2
    }
  },
  "0.15": {
    "full": {
      "avg_tokens_per_turn": 57764.0,
      "avg_total_tokens": 26012147.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 205.1,
      "avg_total_tokens": 90314.0,
      "avg_accuracy": 0.3744
    },
    "msg": {
      "avg_tokens_per_turn": 44.2,
      "avg_total_tokens": 19692.0,
      "avg_accuracy": 0.5554,
      "avg_cue_rate": 0.7559,
      "avg_false_cue_rate": 0.2686,
      "avg_cascade_events": 33.9,
      "avg_socratic_events": 1.3,
      "avg_archived": 1.2
    }
  },
  "0.2": {
    "full": {
      "avg_tokens_per_turn": 47149.9,
      "avg_total_tokens": 18784458.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 214.7,
      "avg_total_tokens": 81591.0,
      "avg_accuracy": 0.3236
    },
    "msg": {
      "avg_tokens_per_turn": 47.8,
      "avg_total_tokens": 18428.0,
      "avg_accuracy": 0.5353,
      "avg_cue_rate": 0.6873,
      "avg_false_cue_rate": 0.2199,
      "avg_cascade_events": 32.7,
      "avg_socratic_events": 0.2,
      "avg_archived": 0.8
    }
  },
  "0.3": {
    "full": {
      "avg_tokens_per_turn": 53826.1,
      "avg_total_tokens": 21513298.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 251.9,
      "avg_total_tokens": 99052.0,
      "avg_accuracy": 0.2638
    },
    "msg": {
      "avg_tokens_per_turn": 37.7,
      "avg_total_tokens": 14486.0,
      "avg_accuracy": 0.4959,
      "avg_cue_rate": 0.6823,
      "avg_false_cue_rate": 0.2768,
      "avg_cascade_events": 50.2,
      "avg_socratic_events": 2.4,
      "avg_archived": 4.0
    }
  },
  "0.4": {
    "full": {
      "avg_tokens_per_turn": 61584.8,
      "avg_total_tokens": 30382977.0,
      "avg_accuracy": 1.0
    },
    "rag": {
      "avg_tokens_per_turn": 189.7,
      "avg_total_tokens": 91312.0,
      "avg_accuracy": 0.1426
    },
    "msg": {
      "avg_tokens_per_turn": 31.2,
      "avg_total_tokens": 14881.0,
      "avg_accuracy": 0.4232,
      "avg_cue_rate": 0.5729,
      "avg_false_cue_rate": 0.2856,
      "avg_cascade_events": 37.7,
      "avg_socratic_events": 5.6,
      "avg_archived": 4.8
    }
  }
}
```

---

