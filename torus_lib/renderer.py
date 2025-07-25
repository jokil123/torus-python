from torus_lib.ray_marcher import Camera, RayMarcher
from torus_lib.screen import Display
from torus_lib.sdf import SDF


class Material:
    pass


class Shader:
    pass


class Scene:
    def __init__(self, camera: Camera, sdf: SDF, material: Material, shader: Shader):
        self.camera = camera
        self.sdf = sdf
        self.material = material
        self.shader = shader

    def update(self, dt: float):
        pass


class Renderer:
    def __init__(self, scene: Scene, display: Display):
        self.scene = scene
        self.display = display

    def render(self, dt: float):
        rays = self.scene.camera.generate_rays()

        RayMarcher(self.scene.sdf, list(itertools.chain.from_iterable(rays)))
