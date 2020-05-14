{
    "input_config": {
        "batch_size": 512,
        "test_size": 0.2
    },
    "model_config": {
        "epsilon": 1e-6,
        "num_clusters": 10,
        "enc_fc11_hidden_dim": 512,
        "enc_fc12_hidden_dim": 512,
        "enc_fc21_hidden_dim": 512,
        "enc_fc22_hidden_dim": 512,
        "enc_gaussian_hidden_dim": 64,
        "dec_gaussian_hidden_dim": 64,
        "dec_fc1_hidden_dim": 512,
        "dec_fc2_hidden_dim": 512,
        "regularization_term_reconstruction": 1.0,
        "regularization_term_gauss": 1.0,
        "regularization_term_category": 1.0
    },
    "training_config": {
        "learning_rate": 0.001,
        "max_iter": 5,
    },
    "evaluation_config": {
    }
}
