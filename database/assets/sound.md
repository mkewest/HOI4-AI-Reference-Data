---
domain: assets
concept: sound
version: 1.14+
requires: []
relates: [interface]
---

# Sound System

Sound definitions control audio playback, mixing, and compression. Files are defined in `sound/*.asset` format (not `.txt`) with separate compressor definitions controlling dynamic range.

> [!CRITICAL] All sound definition files must use `.asset` extension, not `.txt`. Using wrong extension causes files to be ignored entirely with no error message.

## Audio Format Requirements

> [!CRITICAL] Audio files must be in Stereo format but configured as mono channel in the sound definition. This counter-intuitive requirement stems from engine expectations - using actual mono format or setting channel to stereo causes playback issues.

## Sound Definitions

Basic sound definition structure:

```hoi4
sound = {
    name = "example_sound"
    file = "example.wav"
    volume = 0.8
}
```

### Sound Behavior

**max_audible_behaviour**: Only accepts `"fail"` value. No other options are documented or functional. When set to fail, sounds that would exceed maximum audible instances are dropped rather than played.

**random_sound_when_looping**: Controls iteration pattern through sound lists. When false, sounds play iteratively in definition order. When true, sounds are randomly selected each loop. This applies to sound arrays within a single definition.

**prevent_random_repetition**: Only prevents immediate back-to-back repetition when using random selection. Does not prevent A-B-A patterns. If a sound has played, the next random selection cannot pick that same sound, but the sound after may select it again.

Example with random behavior:

```hoi4
sound = {
    name = "random_footsteps"
    file = {
        "footstep1.wav"
        "footstep2.wav"
        "footstep3.wav"
    }
    random_sound_when_looping = yes
    prevent_random_repetition = yes
    volume = 0.6
}
```

The system randomly selects from the three footstep sounds but won't play the same sound twice in a row. It can still produce sequences like footstep1 → footstep2 → footstep1.

## Compressor System

Compressors control dynamic range and volume ducking for different audio categories. Two global compressors exist: `master_compressor` for sound effects and `music_compressor` for music tracks. These are separate audio streams in the engine.

### Global Compressors

```hoi4
master_compressor = {
    threshold = -10.0
    ratio = 4.0
    attack = 0.01
    release = 0.1
}

music_compressor = {
    threshold = -12.0
    ratio = 3.0
    attack = 0.02
    release = 0.15
}
```

Master compressor applies to gameplay sounds while music compressor applies to the music system. They operate independently on their respective audio streams.

### Category Compressors

Sound categories can override global compressors with individual compressor definitions:

```hoi4
category = {
    name = "ui_sounds"
    compressor = {
        enabled = yes
        threshold = -8.0
        ratio = 2.0
        attack = 0.005
        release = 0.05
    }
}
```

The `compressor.enabled` flag only exists in category compressors, not global ones. When enabled, the category compressor overrides global settings for sounds in that category. When disabled or omitted, sounds use global compressor settings.

Category-specific compression enables mixing control - UI sounds can have different dynamic range characteristics than combat sounds or ambient effects.

## Related Systems

Sound system operates independently from most other game systems but integrates with interface for UI sound triggers and events for scripted audio playback.
