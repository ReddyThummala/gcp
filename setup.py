import setuptools

setuptools.setup(
    name='helper_class',
    version='1.0',
    install_requires=['google-cloud-storage','google-cloud-bigquery'],
    packages=['helper_class','batch_pipeline'],
    author='gcpthummala',
    author_email='gcpthummala95@gmail.com')