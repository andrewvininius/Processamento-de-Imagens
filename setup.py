from setuptools import setup, find_packages

setup(
    name='nome_do_pacote',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',  # exemplo de dependência, se necessário
    ],
    author='Seu Nome',
    author_email='seu.email@example.com',
    description='Um pacote de processamento de imagem simples',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='URL_do_repositório_no_GitHub',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
