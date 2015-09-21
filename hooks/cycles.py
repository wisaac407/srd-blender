"""
hooks/cycles.py: All the Cycles-specific hooks.

Copyright (C) 2015 Isaac Weaver
Author: Isaac Weaver <wisaac407@gmail.com>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""


import bpy

from ..SRDRenderHook import SRDRenderHook
from ..SRDRenderer import SRDRenderer


### Seed Group
class SeedHook(SRDRenderHook):
    """Cycles sampling seed."""
    hook_label = 'Seed'
    hook_idname = 'seed'
    hook_group = 'seed'
    hook_render_engine = {'CYCLES'}

    def post_render(self):
        return self.scene.cycles.seed


class SeedAnimatedHook(SRDRenderHook):
    """Weather or not the seed is animated from frame to frame."""
    hook_label = 'Seed is Animated'
    hook_idname = 'animated_seed'
    hook_group = 'seed'
    hook_render_engine = {'CYCLES'}

    def post_render(self):
        return self.scene.cycles.use_animated_seed


## Volume Sampling group
class VolumeStepHook(SRDRenderHook):
    """Cycles volume step size."""
    hook_label = 'Step Size'
    hook_idname = 'step_size'
    hook_group = 'vol_sample'
    hook_render_engine = {'CYCLES'}

    def post_render(self):
        return self.scene.cycles.volume_step_size


class VolumeStepMaxHook(SRDRenderHook):
    """Maximum number of cycles volume steps."""
    hook_label = 'Max Steps'
    hook_idname = 'step_max_size'
    hook_group = 'vol_sample'
    hook_render_engine = {'CYCLES'}

    def post_render(self):
        return self.scene.cycles.volume_max_steps


## Performance group.
class TileSizeHook(SRDRenderHook):
    """Tile size."""
    hook_label = 'Tile Size'
    hook_idname = 'tile_size'
    hook_group = 'perf'
    hook_render_engine = {'CYCLES', 'BLENDER_RENDER'}

    def post_render(self):
        return '%sx%s' % (self.scene.render.tile_x, self.scene.render.tile_y)


class TileOrderHook(SRDRenderHook):
    """Cycles tile order."""
    hook_label = 'Tile Order'
    hook_idname = 'tile_order'
    hook_group = 'perf'
    hook_render_engine = {'CYCLES', 'BLENDER_RENDER'}

    # Dictionary mapping order idname -> order label. i.e. {'CENTER': 'center'}
    orders = dict((idname, label) for idname, label, _ in
        bpy.types.CyclesRenderSettings.tile_order[1]['items'])

    def post_render(self):
        return self.orders[self.scene.cycles.tile_order]


class ThreadsModeHook(SRDRenderHook):
    """Which scheme is used to determine the number of threads."""
    hook_label = 'Threads Mode'
    hook_idname = 'threads_mode'
    hook_group = 'perf'
    hook_render_engine = {'CYCLES', 'BLENDER_RENDER'}

    def post_render(self):
        return self.scene.render.threads_mode.capitalize()


class ThreadsHook(SRDRenderHook):
    """How many threads are being used to render."""
    hook_label = 'Threads'
    hook_idname = 'threads'
    hook_group = 'perf'
    hook_render_engine = {'CYCLES', 'BLENDER_RENDER'}

    def post_render(self):
        return self.scene.render.threads


## Bounces group.
class LBBoundsHook(SRDRenderHook):
    """Bounds of the number of reflection bounces."""
    hook_label = 'Total Bounds'
    hook_idname = 'lb_bounds'
    hook_group = 'light_bounces'
    hook_render_engine = {'CYCLES'}

    def post_render(self):
        return "min: %s, max: %s" % (self.scene.cycles.min_bounces, self.scene.cycles.max_bounces)


class LBDiffuseHook(SRDRenderHook):
    """Maximum number of diffuse reflection bounces."""
    hook_label = 'Diffuse'
    hook_idname = 'lb_diffuse'
    hook_group = 'light_bounces'
    hook_render_engine = {'CYCLES'}

    def post_render(self):
        return self.scene.cycles.diffuse_bounces


class LBGlossyHook(SRDRenderHook):
    """Maximum number of glossy reflection bounces."""
    hook_label = 'Glossy'
    hook_idname = 'lb_glossy'
    hook_group = 'light_bounces'
    hook_render_engine = {'CYCLES'}

    def post_render(self):
        return self.scene.cycles.glossy_bounces


class LBTransHook(SRDRenderHook):
    """Maximum number of transmission reflection bounces."""
    hook_label = 'Transmission'
    hook_idname = 'lb_trans'
    hook_group = 'light_bounces'
    hook_render_engine = {'CYCLES'}

    def post_render(self):
        return self.scene.cycles.transmission_bounces


class LBVolumeHook(SRDRenderHook):
    """Maximum number of volume reflection bounces."""
    hook_label = 'Volume'
    hook_idname = 'lb_volume'
    hook_group = 'light_bounces'
    hook_render_engine = {'CYCLES'}

    def post_render(self):
        return self.scene.cycles.volume_bounces


class LPShadowsHook(SRDRenderHook):
    """Use transparency of surfaces for rendering shadows."""
    hook_label = 'Shadows'
    hook_idname = 'lp_shadows'
    hook_group = 'light_paths'
    hook_render_engine = {'CYCLES'}

    def post_render(self):
        return self.scene.cycles.use_transparent_shadows


class LPCausticsReflectiveHook(SRDRenderHook):
    """Using reflective caustics."""
    hook_label = 'Reflective Caustics'
    hook_idname = 'lp_caustics_reflective'
    hook_group = 'light_paths'
    hook_render_engine = {'CYCLES'}

    def post_render(self):
        return self.scene.cycles.caustics_reflective


class LPCausticsRefractiveHook(SRDRenderHook):
    """Using refractive caustics."""
    hook_label = 'Refractive Caustics'
    hook_idname = 'lp_caustics_refractive'
    hook_group = 'light_paths'
    hook_render_engine = {'CYCLES'}

    def post_render(self):
        return self.scene.cycles.caustics_refractive


class LPFilterGlossyHook(SRDRenderHook):
    """Cycles filter glossy threshold."""
    hook_label = 'Filter Glossy'
    hook_idname = 'lp_filter_glossy'
    hook_group = 'light_paths'
    hook_render_engine = {'CYCLES'}

    def post_render(self):
        return self.scene.cycles.blur_glossy


## Sampling group
class SMSamplesHook(SRDRenderHook):
    """Number of cycles samples used(accounting for square samples)."""
    hook_label = 'Samples'
    hook_idname = 'sm_samples'
    hook_group = 'sampling'
    hook_render_engine = {'CYCLES'}

    def post_render(self):
        samples = self.scene.cycles.samples
        square_samples = self.scene.cycles.use_square_samples
        # If we are using square samples then square the output.
        return samples * samples if square_samples else samples


class SMClampDirectHook(SRDRenderHook):
    """How much we are clamping direct light."""
    hook_label = 'Clamp Direct'
    hook_idname = 'sm_clamp_direct'
    hook_group = 'sampling'
    hook_render_engine = {'CYCLES'}

    def post_render(self):
        return self.scene.cycles.sample_clamp_direct


class SMClampIndirectHook(SRDRenderHook):
    """How much we are clamping indirect light."""
    hook_label = 'Clamp Indirect'
    hook_idname = 'sm_clamp_indirect'
    hook_group = 'sampling'
    hook_render_engine = {'CYCLES'}

    def post_render(self):
        return self.scene.cycles.sample_clamp_indirect


def register():
    # Seed group.
    SRDRenderer.register_group('seed', 'Seed')
    SRDRenderer.register_hook(SeedHook)
    SRDRenderer.register_hook(SeedAnimatedHook)

    # Volume sampling group.
    SRDRenderer.register_group('vol_sample', 'Volume Sampling')
    SRDRenderer.register_hook(VolumeStepHook)
    SRDRenderer.register_hook(VolumeStepMaxHook)

    # Performance group.
    SRDRenderer.register_group('perf', 'Performance')
    SRDRenderer.register_hook(TileSizeHook)
    SRDRenderer.register_hook(TileOrderHook)
    SRDRenderer.register_hook(ThreadsModeHook)
    SRDRenderer.register_hook(ThreadsHook)

    # Bounces group.
    SRDRenderer.register_group('light_bounces', 'Bounces')
    SRDRenderer.register_hook(LBBoundsHook)
    SRDRenderer.register_hook(LBDiffuseHook)
    SRDRenderer.register_hook(LBGlossyHook)
    SRDRenderer.register_hook(LBTransHook)
    SRDRenderer.register_hook(LBVolumeHook)

    # Light Paths group.
    SRDRenderer.register_group('light_paths', 'Light Paths')
    SRDRenderer.register_hook(LPShadowsHook)
    SRDRenderer.register_hook(LPCausticsReflectiveHook)
    SRDRenderer.register_hook(LPCausticsRefractiveHook)
    SRDRenderer.register_hook(LPFilterGlossyHook)

    # Sampling group
    SRDRenderer.register_group('sampling', 'Sampling')
    SRDRenderer.register_hook(SMSamplesHook)
    SRDRenderer.register_hook(SMClampDirectHook)
    SRDRenderer.register_hook(SMClampIndirectHook)
