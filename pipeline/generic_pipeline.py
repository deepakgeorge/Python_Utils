
class GenericPipeline:
    def __init__(self,
                 pipeline_components=None):
        """
        :param pipeline_components: List of tuples (name, component function)
        """
        self.pipeline_components = pipeline_components if pipeline_components else []

    def __getitem__(self, item):

        for component in self.pipeline_components:
            component_transform = component[1]
            item = component_transform(item)
        return item

    def __call__(self, item, *args, **kwargs):
        return self[item]

    def add_component(self, component):
        self.pipeline_components.append(component)

    def remove_component(self, name):
        self.pipeline_components = [cp for cp in self.pipeline_components if cp[0] != name]

    def get_component(self, name):
        return [cp[1] for cp in self.pipeline_components if cp[0] == name]