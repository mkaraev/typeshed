"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Protocol messages for describing the results of benchmarks and unit tests."""

import builtins
import collections.abc
import sys
import typing

import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.wrappers_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class EntryValue(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOUBLE_VALUE_FIELD_NUMBER: builtins.int
    STRING_VALUE_FIELD_NUMBER: builtins.int
    double_value: builtins.float
    string_value: builtins.str
    def __init__(self, *, double_value: builtins.float | None = ..., string_value: builtins.str | None = ...) -> None: ...
    def HasField(
        self, field_name: typing.Literal["double_value", b"double_value", "kind", b"kind", "string_value", b"string_value"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing.Literal["double_value", b"double_value", "kind", b"kind", "string_value", b"string_value"]
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing.Literal["kind", b"kind"]
    ) -> typing.Literal["double_value", "string_value"] | None: ...

global___EntryValue = EntryValue

@typing.final
class MetricEntry(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    MIN_VALUE_FIELD_NUMBER: builtins.int
    MAX_VALUE_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Metric name"""
    value: builtins.float
    """Metric value"""
    @property
    def min_value(self) -> google.protobuf.wrappers_pb2.DoubleValue:
        """The minimum acceptable value for the metric if specified"""

    @property
    def max_value(self) -> google.protobuf.wrappers_pb2.DoubleValue:
        """The maximum acceptable value for the metric if specified"""

    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
        value: builtins.float | None = ...,
        min_value: google.protobuf.wrappers_pb2.DoubleValue | None = ...,
        max_value: google.protobuf.wrappers_pb2.DoubleValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["max_value", b"max_value", "min_value", b"min_value"]) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing.Literal["max_value", b"max_value", "min_value", b"min_value", "name", b"name", "value", b"value"]
    ) -> None: ...

global___MetricEntry = MetricEntry

@typing.final
class BenchmarkEntry(google.protobuf.message.Message):
    """Each unit test or benchmark in a test or benchmark run provides
    some set of information.  Here we provide some reasonable keys
    one would expect to see, with optional key/value pairs for things
    we haven't considered.

    This BenchmarkEntry should be emitted by each unit test or benchmark
    reporter.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class ExtrasEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___EntryValue: ...
        def __init__(self, *, key: builtins.str | None = ..., value: global___EntryValue | None = ...) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    ITERS_FIELD_NUMBER: builtins.int
    CPU_TIME_FIELD_NUMBER: builtins.int
    WALL_TIME_FIELD_NUMBER: builtins.int
    THROUGHPUT_FIELD_NUMBER: builtins.int
    EXTRAS_FIELD_NUMBER: builtins.int
    METRICS_FIELD_NUMBER: builtins.int
    name: builtins.str
    """The name of the specific benchmark or test
    (e.g. BM_AdjustContrast_gpu_B_W_H)
    """
    iters: builtins.int
    """If a benchmark, how many iterations it was run for"""
    cpu_time: builtins.float
    """Total cpu time used for all iterations (in seconds)"""
    wall_time: builtins.float
    """Total wall time used for all iterations (in seconds)"""
    throughput: builtins.float
    """Throughput (in MB/s)"""
    @property
    def extras(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___EntryValue]:
        """Generic map from result key to value."""

    @property
    def metrics(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MetricEntry]:
        """Metric name, value and expected range. This can include accuracy metrics
        typically used to determine whether the accuracy test has passed
        """

    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
        iters: builtins.int | None = ...,
        cpu_time: builtins.float | None = ...,
        wall_time: builtins.float | None = ...,
        throughput: builtins.float | None = ...,
        extras: collections.abc.Mapping[builtins.str, global___EntryValue] | None = ...,
        metrics: collections.abc.Iterable[global___MetricEntry] | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "cpu_time",
            b"cpu_time",
            "extras",
            b"extras",
            "iters",
            b"iters",
            "metrics",
            b"metrics",
            "name",
            b"name",
            "throughput",
            b"throughput",
            "wall_time",
            b"wall_time",
        ],
    ) -> None: ...

global___BenchmarkEntry = BenchmarkEntry

@typing.final
class BenchmarkEntries(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENTRY_FIELD_NUMBER: builtins.int
    @property
    def entry(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BenchmarkEntry]: ...
    def __init__(self, *, entry: collections.abc.Iterable[global___BenchmarkEntry] | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["entry", b"entry"]) -> None: ...

global___BenchmarkEntries = BenchmarkEntries

@typing.final
class BuildConfiguration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODE_FIELD_NUMBER: builtins.int
    CC_FLAGS_FIELD_NUMBER: builtins.int
    OPTS_FIELD_NUMBER: builtins.int
    mode: builtins.str
    """opt, dbg, etc"""
    @property
    def cc_flags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """CC compiler flags, if known"""

    @property
    def opts(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Bazel compilation options, if known"""

    def __init__(
        self,
        *,
        mode: builtins.str | None = ...,
        cc_flags: collections.abc.Iterable[builtins.str] | None = ...,
        opts: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cc_flags", b"cc_flags", "mode", b"mode", "opts", b"opts"]) -> None: ...

global___BuildConfiguration = BuildConfiguration

@typing.final
class CommitId(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHANGELIST_FIELD_NUMBER: builtins.int
    HASH_FIELD_NUMBER: builtins.int
    SNAPSHOT_FIELD_NUMBER: builtins.int
    PENDING_CHANGELIST_FIELD_NUMBER: builtins.int
    changelist: builtins.int
    """Submitted changelist."""
    hash: builtins.str
    snapshot: builtins.str
    """Hash of intermediate change between hash/changelist and what was tested.
    Not used if the build is from a commit without modifications.
    """
    pending_changelist: builtins.int
    """Changelist tested if the change list is not already submitted."""
    def __init__(
        self,
        *,
        changelist: builtins.int | None = ...,
        hash: builtins.str | None = ...,
        snapshot: builtins.str | None = ...,
        pending_changelist: builtins.int | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing.Literal["changelist", b"changelist", "hash", b"hash", "kind", b"kind"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "changelist",
            b"changelist",
            "hash",
            b"hash",
            "kind",
            b"kind",
            "pending_changelist",
            b"pending_changelist",
            "snapshot",
            b"snapshot",
        ],
    ) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["kind", b"kind"]) -> typing.Literal["changelist", "hash"] | None: ...

global___CommitId = CommitId

@typing.final
class CPUInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class CacheSizeEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.int
        def __init__(self, *, key: builtins.str | None = ..., value: builtins.int | None = ...) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    NUM_CORES_FIELD_NUMBER: builtins.int
    NUM_CORES_ALLOWED_FIELD_NUMBER: builtins.int
    MHZ_PER_CPU_FIELD_NUMBER: builtins.int
    CPU_INFO_FIELD_NUMBER: builtins.int
    CPU_GOVERNOR_FIELD_NUMBER: builtins.int
    CACHE_SIZE_FIELD_NUMBER: builtins.int
    num_cores: builtins.int
    num_cores_allowed: builtins.int
    mhz_per_cpu: builtins.float
    """How fast are these cpus?"""
    cpu_info: builtins.str
    """Additional cpu information. For example,
    Intel Ivybridge with HyperThreading (24 cores) dL1:32KB dL2:256KB dL3:30MB
    """
    cpu_governor: builtins.str
    """What kind of cpu scaling is enabled on the host.
    Examples include "performance", "ondemand", "conservative", "mixed".
    """
    @property
    def cache_size(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.int]:
        """Cache sizes (in bytes), e.g. "L2": 262144 (for 256KB)"""

    def __init__(
        self,
        *,
        num_cores: builtins.int | None = ...,
        num_cores_allowed: builtins.int | None = ...,
        mhz_per_cpu: builtins.float | None = ...,
        cpu_info: builtins.str | None = ...,
        cpu_governor: builtins.str | None = ...,
        cache_size: collections.abc.Mapping[builtins.str, builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "cache_size",
            b"cache_size",
            "cpu_governor",
            b"cpu_governor",
            "cpu_info",
            b"cpu_info",
            "mhz_per_cpu",
            b"mhz_per_cpu",
            "num_cores",
            b"num_cores",
            "num_cores_allowed",
            b"num_cores_allowed",
        ],
    ) -> None: ...

global___CPUInfo = CPUInfo

@typing.final
class MemoryInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOTAL_FIELD_NUMBER: builtins.int
    AVAILABLE_FIELD_NUMBER: builtins.int
    total: builtins.int
    """Total virtual memory in bytes"""
    available: builtins.int
    """Immediately available memory in bytes"""
    def __init__(self, *, total: builtins.int | None = ..., available: builtins.int | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["available", b"available", "total", b"total"]) -> None: ...

global___MemoryInfo = MemoryInfo

@typing.final
class GPUInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODEL_FIELD_NUMBER: builtins.int
    UUID_FIELD_NUMBER: builtins.int
    BUS_ID_FIELD_NUMBER: builtins.int
    model: builtins.str
    """e.g. "Tesla K40c" """
    uuid: builtins.str
    """Final entry in output of "nvidia-smi -L" """
    bus_id: builtins.str
    """e.g. "0000:04:00.0" """
    def __init__(
        self, *, model: builtins.str | None = ..., uuid: builtins.str | None = ..., bus_id: builtins.str | None = ...
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["bus_id", b"bus_id", "model", b"model", "uuid", b"uuid"]) -> None: ...

global___GPUInfo = GPUInfo

@typing.final
class PlatformInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BITS_FIELD_NUMBER: builtins.int
    LINKAGE_FIELD_NUMBER: builtins.int
    MACHINE_FIELD_NUMBER: builtins.int
    RELEASE_FIELD_NUMBER: builtins.int
    SYSTEM_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    bits: builtins.str
    """e.g. '64bit'"""
    linkage: builtins.str
    """e.g. 'ELF'"""
    machine: builtins.str
    """e.g. 'i386'"""
    release: builtins.str
    """e.g. '3.13.0-76-generic'"""
    system: builtins.str
    """e.g. 'Linux'"""
    version: builtins.str
    """e.g. '#120-Ubuntu SMP Mon Jan 18 15:59:10 UTC 2016'"""
    def __init__(
        self,
        *,
        bits: builtins.str | None = ...,
        linkage: builtins.str | None = ...,
        machine: builtins.str | None = ...,
        release: builtins.str | None = ...,
        system: builtins.str | None = ...,
        version: builtins.str | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "bits",
            b"bits",
            "linkage",
            b"linkage",
            "machine",
            b"machine",
            "release",
            b"release",
            "system",
            b"system",
            "version",
            b"version",
        ],
    ) -> None: ...

global___PlatformInfo = PlatformInfo

@typing.final
class AvailableDeviceInfo(google.protobuf.message.Message):
    """Matches DeviceAttributes"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    MEMORY_LIMIT_FIELD_NUMBER: builtins.int
    PHYSICAL_DESCRIPTION_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Device name."""
    type: builtins.str
    """Device type, e.g. 'CPU' or 'GPU'."""
    memory_limit: builtins.int
    """Memory capacity in bytes."""
    physical_description: builtins.str
    """The physical description of this device."""
    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
        type: builtins.str | None = ...,
        memory_limit: builtins.int | None = ...,
        physical_description: builtins.str | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "memory_limit", b"memory_limit", "name", b"name", "physical_description", b"physical_description", "type", b"type"
        ],
    ) -> None: ...

global___AvailableDeviceInfo = AvailableDeviceInfo

@typing.final
class MachineConfiguration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOSTNAME_FIELD_NUMBER: builtins.int
    SERIAL_IDENTIFIER_FIELD_NUMBER: builtins.int
    PLATFORM_INFO_FIELD_NUMBER: builtins.int
    CPU_INFO_FIELD_NUMBER: builtins.int
    DEVICE_INFO_FIELD_NUMBER: builtins.int
    AVAILABLE_DEVICE_INFO_FIELD_NUMBER: builtins.int
    MEMORY_INFO_FIELD_NUMBER: builtins.int
    hostname: builtins.str
    """Host name of machine that ran the benchmark."""
    serial_identifier: builtins.str
    """Unique serial number of the machine."""
    @property
    def platform_info(self) -> global___PlatformInfo:
        """Additional platform information."""

    @property
    def cpu_info(self) -> global___CPUInfo:
        """CPU Information."""

    @property
    def device_info(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]:
        """Other devices that are attached and relevant (e.g. GPUInfo)."""

    @property
    def available_device_info(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AvailableDeviceInfo]:
        """Devices accessible to the test (e.g. as given by list_local_devices)."""

    @property
    def memory_info(self) -> global___MemoryInfo: ...
    def __init__(
        self,
        *,
        hostname: builtins.str | None = ...,
        serial_identifier: builtins.str | None = ...,
        platform_info: global___PlatformInfo | None = ...,
        cpu_info: global___CPUInfo | None = ...,
        device_info: collections.abc.Iterable[google.protobuf.any_pb2.Any] | None = ...,
        available_device_info: collections.abc.Iterable[global___AvailableDeviceInfo] | None = ...,
        memory_info: global___MemoryInfo | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal["cpu_info", b"cpu_info", "memory_info", b"memory_info", "platform_info", b"platform_info"],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "available_device_info",
            b"available_device_info",
            "cpu_info",
            b"cpu_info",
            "device_info",
            b"device_info",
            "hostname",
            b"hostname",
            "memory_info",
            b"memory_info",
            "platform_info",
            b"platform_info",
            "serial_identifier",
            b"serial_identifier",
        ],
    ) -> None: ...

global___MachineConfiguration = MachineConfiguration

@typing.final
class RunConfiguration(google.protobuf.message.Message):
    """Run-specific items such as arguments to the test / benchmark."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class EnvVarsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(self, *, key: builtins.str | None = ..., value: builtins.str | None = ...) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    ARGUMENT_FIELD_NUMBER: builtins.int
    ENV_VARS_FIELD_NUMBER: builtins.int
    @property
    def argument(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def env_vars(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Environment variables used to run the test/benchmark."""

    def __init__(
        self,
        *,
        argument: collections.abc.Iterable[builtins.str] | None = ...,
        env_vars: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["argument", b"argument", "env_vars", b"env_vars"]) -> None: ...

global___RunConfiguration = RunConfiguration

@typing.final
class TestResults(google.protobuf.message.Message):
    """The output of one benchmark / test run.  Each run contains a list of
    tests or benchmarks, stored as BenchmarkEntry messages.

    This message should be emitted by the reporter (which runs the
    test / BM in a subprocess and then reads the emitted BenchmarkEntry messages;
    usually from a serialized json file, finally collecting them along
    with additional information about the test run.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _BenchmarkType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _BenchmarkTypeEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[TestResults._BenchmarkType.ValueType], builtins.type
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: TestResults._BenchmarkType.ValueType  # 0
        """Fallback for protos written before Type was introduced."""
        CPP_MICROBENCHMARK: TestResults._BenchmarkType.ValueType  # 1
        PYTHON_BENCHMARK: TestResults._BenchmarkType.ValueType  # 2
        ANDROID_BENCHMARK: TestResults._BenchmarkType.ValueType  # 3
        EDGE_BENCHMARK: TestResults._BenchmarkType.ValueType  # 4
        IOS_BENCHMARK: TestResults._BenchmarkType.ValueType  # 5

    class BenchmarkType(_BenchmarkType, metaclass=_BenchmarkTypeEnumTypeWrapper):
        """The type of benchmark."""

    UNKNOWN: TestResults.BenchmarkType.ValueType  # 0
    """Fallback for protos written before Type was introduced."""
    CPP_MICROBENCHMARK: TestResults.BenchmarkType.ValueType  # 1
    PYTHON_BENCHMARK: TestResults.BenchmarkType.ValueType  # 2
    ANDROID_BENCHMARK: TestResults.BenchmarkType.ValueType  # 3
    EDGE_BENCHMARK: TestResults.BenchmarkType.ValueType  # 4
    IOS_BENCHMARK: TestResults.BenchmarkType.ValueType  # 5

    TARGET_FIELD_NUMBER: builtins.int
    ENTRIES_FIELD_NUMBER: builtins.int
    BUILD_CONFIGURATION_FIELD_NUMBER: builtins.int
    COMMIT_ID_FIELD_NUMBER: builtins.int
    START_TIME_FIELD_NUMBER: builtins.int
    RUN_TIME_FIELD_NUMBER: builtins.int
    MACHINE_CONFIGURATION_FIELD_NUMBER: builtins.int
    RUN_CONFIGURATION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    BENCHMARK_TYPE_FIELD_NUMBER: builtins.int
    RUN_MODE_FIELD_NUMBER: builtins.int
    TF_VERSION_FIELD_NUMBER: builtins.int
    target: builtins.str
    """The target of the run, e.g.:
     //tensorflow/core:kernels_adjust_contrast_op_benchmark_test
    """
    start_time: builtins.int
    """The time the run started (in seconds of UTC time since Unix epoch)"""
    run_time: builtins.float
    """The amount of time the total run took (wall time in seconds)"""
    name: builtins.str
    """Benchmark target identifier."""
    benchmark_type: global___TestResults.BenchmarkType.ValueType
    run_mode: builtins.str
    """Used for differentiating between continuous and debug builds.
    Must be one of:
    * cbuild: results from continuous build.
    * presubmit: results from oneshot requests.
    * culprit: results from culprit finder rerun.
    """
    tf_version: builtins.str
    """TensorFlow version this benchmark runs against.
    This can be either set to full version or just the major version.
    """
    @property
    def entries(self) -> global___BenchmarkEntries:
        """The list of tests or benchmarks in this run."""

    @property
    def build_configuration(self) -> global___BuildConfiguration:
        """The configuration of the build (compiled opt? with cuda? any copts?)"""

    @property
    def commit_id(self) -> global___CommitId:
        """The commit id (git hash or changelist)"""

    @property
    def machine_configuration(self) -> global___MachineConfiguration:
        """Machine-specific parameters (Platform and CPU info)"""

    @property
    def run_configuration(self) -> global___RunConfiguration:
        """Run-specific parameters (arguments, etc)"""

    def __init__(
        self,
        *,
        target: builtins.str | None = ...,
        entries: global___BenchmarkEntries | None = ...,
        build_configuration: global___BuildConfiguration | None = ...,
        commit_id: global___CommitId | None = ...,
        start_time: builtins.int | None = ...,
        run_time: builtins.float | None = ...,
        machine_configuration: global___MachineConfiguration | None = ...,
        run_configuration: global___RunConfiguration | None = ...,
        name: builtins.str | None = ...,
        benchmark_type: global___TestResults.BenchmarkType.ValueType | None = ...,
        run_mode: builtins.str | None = ...,
        tf_version: builtins.str | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "build_configuration",
            b"build_configuration",
            "commit_id",
            b"commit_id",
            "entries",
            b"entries",
            "machine_configuration",
            b"machine_configuration",
            "run_configuration",
            b"run_configuration",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "benchmark_type",
            b"benchmark_type",
            "build_configuration",
            b"build_configuration",
            "commit_id",
            b"commit_id",
            "entries",
            b"entries",
            "machine_configuration",
            b"machine_configuration",
            "name",
            b"name",
            "run_configuration",
            b"run_configuration",
            "run_mode",
            b"run_mode",
            "run_time",
            b"run_time",
            "start_time",
            b"start_time",
            "target",
            b"target",
            "tf_version",
            b"tf_version",
        ],
    ) -> None: ...

global___TestResults = TestResults
