import setuptools

setuptools.setup(
    name='batch_pipeline',
    version='1.0',
    install_requires=['google-cloud-storage','google-cloud-bigquery'],
    packages=['batch_pipeline','helper_class'],
    author='gcpthummala',
    author_email='gcpthummala95@gmail.com')