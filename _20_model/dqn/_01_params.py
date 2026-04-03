def get_train_params():
    """====================================================================================================
    ## Hyperparameter Setting for training
    ===================================================================================================="""
    # Define the training parameters
    TRAIN_PARAMS = {
    "learning_rate": 1e-4,
    "gamma": 0.99,
    "epsilon_start": 1.0,
    "epsilon_end": 0.03,
    "epsilon_decay": 0.999985,
    "replay_buffer_size": 300000,
    "replay_start_size": 20000,
    "batch_size": 128,
    "hidden_dim": 256,
    "hidden_layer_count": 2,
    "target_update_interval": 3000,
    "epsilon_init": None,
    "training_steps_init": 0,
    "max_steps_per_episode": 30*60*3,
    "show_progress": True,
    "progress_interval": 50,
}


    # Return the training parameters
    return TRAIN_PARAMS


def get_play_params():
    """====================================================================================================
    ## Hyperparameter Setting for Playing
    ===================================================================================================="""
    # Define the play parameters
    PLAY_PARAMS = {
        # Maximum Steps per Episode
        "max_steps": 30*60*60,
    }

    # Return the play parameters
    return PLAY_PARAMS