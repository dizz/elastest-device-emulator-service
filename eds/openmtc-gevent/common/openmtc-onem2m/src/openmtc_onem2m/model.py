from enum import IntEnum, unique

from openmtc.model import (Resource as Res, UnicodeAttribute, DatetimeAttribute,
                           Attribute, ListAttribute, Entity, EntityAttribute,
                           AnyURI, StringListAttribute, ContentResource)
from openmtc.model.exc import ModelTypeError
from futile import issubclass

LATEST_VERSION = "1.6"


class OneM2MIntEnum(IntEnum):
    def __str__(self):
        return str(self.value)


class OneM2MEntity(Entity):
    pass


class OneM2MContentResource(ContentResource, OneM2MEntity):
    pass


class OneM2MResource(Res, OneM2MEntity):
    __model_name__ = "onem2m"
    __model_version__ = "1.6"


################################################################################
# enumerationTypes
################################################################################

class ResourceTypeE(OneM2MIntEnum):
    accessControlPolicy = 1
    AE = 2
    container = 3
    contentInstance = 4
    CSEBase = 5
    delivery = 6
    eventConfig = 7
    execInstance = 8
    group = 9
    localPolicy = 10
    m2mServiceSubscriptionProfile = 11
    mgmtCmd = 12
    mgmtObj = 13
    node = 14
    pollingChannel = 15
    remoteCSE = 16
    request = 17
    schedule = 18
    serviceSubscribedAppRule = 19
    serviceSubscribedNode = 20
    statsCollect = 21
    statsConfig = 22
    subscription = 23
    accessControlPolicyAnnc = 10001
    AEAnnc = 10002
    containerAnnc = 10003
    contentInstanceAnnc = 10004
    groupAnnc = 10009
    locationPolicyAnnc = 10010
    mgmtObjAnnc = 10013
    nodeAnnc = 10014
    remoteCSEAnnc = 10016
    scheduleAnnc = 10018


@unique
class CSETypeIDE(OneM2MIntEnum):
    IN_CSE = 1
    MN_CSE = 2
    AEN_CSE = 3


@unique
class LocationSourceE(OneM2MIntEnum):
    Network_based = 1
    Device_based = 2
    Sharing_based = 3


@unique
class StdEventCatsE(OneM2MIntEnum):
    mmediate = 2
    BestEffort = 3
    Latest = 4


@unique
class OperationE(OneM2MIntEnum):
    Create = 1
    Retrieve = 2
    Update = 3
    Delete = 4
    Notify = 5


@unique
class ResponseType(OneM2MIntEnum):
    nonBlockingRequestSynch = 1
    nonBlockingRequestAsynch = 2
    blockingRequest = 3


# @unique
# class ResultConentE(OneM2MIntEnum):
#    nothing = 0
#    attributes = 1
#    hierarchical_address = 2
#    hierarchical_address_and_attributes = 3
#    attributes_and_child_resources = 4
#    attributes_and_child_resource_references = 6
#    child_resource_references = 6
#    original_resource = 7


@unique
class DiscResTypeE(OneM2MIntEnum):
    structured = 1
    unstructured = 2


# TODO: responseStatusCode


@unique
class RequestStatusE(OneM2MIntEnum):
    COMPLETED = 1
    FAILED = 2
    PENDING = 3
    FORWARDED = 4


@unique
class MemberTypeE(OneM2MIntEnum):
    accessControlPolicy = 1
    AE = 2
    container = 3
    contentInstance = 4
    CSEBase = 5
    delivery = 6
    eventConfig = 7
    execInstance = 8
    group = 9
    locationPolicy = 10
    m2mServiceSubscription = 11
    mgmtCmd = 12
    mgmtObj = 13
    node = 14
    pollingChannel = 15
    remoteCSE = 16
    request = 17
    schedule = 18
    serviceSubscribedAppRule = 19
    serviceSubscribedNode = 20
    statsCollect = 21
    statsConfig = 22
    subscription = 23
    accessControlPolicyAnnc = 10001
    AEAnnc = 10002
    containerAnnc = 10003
    contentInstanceAnnc = 10004
    groupAnnc = 10009
    locationPolicyAnnc = 10010
    mgmtObjAnnc = 10013
    nodeAnnc = 10014
    remoteCSEAnnc = 10016
    scheduleAnnc = 10019
    mixed = 24
    # Mixed is a mixture of the resource types from 1 to 23, 10001 to 10004, 10009 to  10010,
    # 10013 to 10014 and 10016 to 10018 as listed above.


@unique
class ConsistencyStrategyE(OneM2MIntEnum):
    ABANDON_MEMBER = 1
    ABANDON_GROUP = 2
    SET_MIXED = 3


@unique
class CmdTypeE(OneM2MIntEnum):
    RESET = 1
    REBOOT = 2
    UPLOAD = 3
    DOWNLOAD = 4
    SOFTWAREINSTALL = 5
    SOFTWAREUNINSTALL = 6
    SOFTWAREUPDATE = 7


@unique
class ExecModeTypeE(OneM2MIntEnum):
    MMEDIATEONCE = 1
    IMMEDIATEREPEAT = 2
    RANDOMONCE = 3
    RANDOMREPEAT = 4


@unique
class ExecStatusTypeE(OneM2MIntEnum):
    INITIATED = 1
    PENDING = 2
    FINISHED = 3
    CANCELLING = 4
    CANCELLED = 5
    STATUS_NON_CANCELLABLE = 6


@unique
class ExecResultTypeE(OneM2MIntEnum):
    STATUS_REQUEST_UNSUPPORTED = 1
    STATUS_REQUEST_DENIED = 2
    STATUS_CANCELLATION_DENIED = 3
    STATUS_INTERNAL_ERROR = 4
    STATUS_INVALID_ARGUMENTS = 5
    STATUS_RESOURCES_EXCEEDED = 6
    STATUS_FILE_TRANSFER_FAILED = 7
    STATUS_FILE_TRANSFER_SERVER_AUTHENTICATION_FAILURE = 8
    STATUS_UNSUPPORTED_PROTOCOL = 9
    STATUS_UPLOAD_FAILED = 10
    STATUS_FILE_TRANSFER_FAILED_MULTICAST_GROUP_UNABLE_JOIN = 11
    STATUS_FILE_TRANSFER_FAILED_SERVER_CONTACT_FAILED = 12
    STATUS_FILE_TRANSFER_FAILED_FILE_ACCESS_FAILED = 13
    STATUS_FILE_TRANSFER_FAILED_DOWNLOAD_INCOMPLETE = 14
    STATUS_FILE_TRANSFER_FAILED_FILE_CORRUPTED = 15
    STATUS_FILE_TRANSFER_FILE_AUTHENTICATION_FAILURE = 16
    STATUS_FILE_TRANSFER_WINDOW_EXCEEDED = 19
    STATUS_INVALID_UUID_FORMAT = 20
    STATUS_UNKNOWN_EXECUTION_ENVIRONMENT = 21
    STATUS_DISABLED_EXECUTION_ENVIRONMENT = 22
    STATUS_EXECUTION_ENVIRONMENT_MISMATCH = 23
    STATUS_DUPLICATE_DEPLOYMENT_UNIT = 24
    STATUS_SYSTEM_RESOURCES_EXCEEDED = 25
    STATUS_UNKNOWN_DEPLOYMENT_UNIT = 26
    STATUS_INVALID_DEPLOYMENT_UNIT_STATE = 27
    STATUS_INVALID_DEPLOYMENT_UNIT_UPDATE_DOWNGRADE_DISALLOWED = 28
    STATUS_INVALID_DEPLOYMENT_UNIT_UPDATE_UPGRADE_DISALLOWED = 29
    STATUS_INVALID_DEPLOYMENT_UNIT_UPDATE_VERSION_EXISTS = 30


@unique
class PendingNotificationE(OneM2MIntEnum):
    sendLatest = 1
    sendAllPending = 2


@unique
class NotificationContentTypeE(OneM2MIntEnum):
    allAttributes = 1
    modifiedAttributes = 2
    resourceID = 3


@unique
class NotificationEventTypeE(OneM2MIntEnum):
    updateOfResource = 1
    deleteOfResource = 2
    createOfDirectChildResource = 3
    deleteOfDirectChildResource = 4


@unique
class StatusE(OneM2MIntEnum):
    Successful = 1
    Failure = 2
    In_Process = 3


@unique
class BatteryStatusE(OneM2MIntEnum):
    NORMAL = 1
    CHARGING = 2
    CHARGING_COMPLETE = 3
    DAMAGED = 4
    LOW_BATTERY = 5
    NOT_INSTALLED = 6
    UNKNOWN = 7


@unique
class ManagementDefinitionE(OneM2MIntEnum):
    firmware = 1001
    software = 1002
    memory = 1003
    areaNwkInfo = 1004
    areaNwkDeviceInfo = 1005
    battery = 1006
    deviceInfo = 1007
    deviceCapability = 1008
    reboot = 1009
    eventLog = 1010
    cmdhPolicy = 1011
    activeCmdhPolicy = 1012
    cmdhDefaults = 1013
    cmdhDefEcValue = 1014
    cmdhEcDefParamValues = 1015
    cmdhLimits = 1016
    cmdhNetworkAccessRules = 1017
    cmdhNwAccessRule = 1018
    cmdhBuffer = 1019
    Unspecified = 0


@unique
class LogTypeIdE(OneM2MIntEnum):
    System = 1
    Security = 2
    Event = 3
    Trace = 4
    Panic = 5


@unique
class LogStatusE(OneM2MIntEnum):
    Started = 1
    Stopped = 2
    Unknown = 3
    NotPresent = 4
    Error = 5


@unique
class EventTypeE(OneM2MIntEnum):
    DATAOPERATION = 1
    STORAGEBASED = 2
    TIMERBASED = 3


@unique
class StatsRuleStatusTypeE(OneM2MIntEnum):
    ACTIVE = 1
    INACTIVE = 2


@unique
class StatModelTypeE(OneM2MIntEnum):
    EVENTBASED = 1


@unique
class EncodingTypeE(OneM2MIntEnum):
    plain = 0
    base64String = 1
    base64Binary = 2


@unique
class AccessControlOperationE(OneM2MIntEnum):
    create = 1
    retrieve = 2
    update = 3
    delete = 4
    notify = 5
    discover = 6

# TODO: SRole-ID


@unique
class FilterUsageE(OneM2MIntEnum):
    Discovery = 1
    ConditionalRetrieval = 2


@unique
class CountryCodeE(OneM2MIntEnum):
    india = 91
    usa = 01


################################################################################
# commonTypes
################################################################################

# simple #######################################################################


class IDS(UnicodeAttribute):
    pass

# TODO: nodeID

# TODO: deviceID

# TODO: externalID


class RequestIDS(UnicodeAttribute):
    pass


class NhURIS(UnicodeAttribute):
    pass

# TODO: acpType


class LabelsS(StringListAttribute):
    pass

# TODO: triggerRecipientID

# TODO: listOfM2MID

# TODO: longMin-1

# TODO: listOfMinMax

# TODO: backOffParameters

# TODO: poaList


class TimestampS(DatetimeAttribute):
    pass

# TODO: absRelTimestamp

# TODO: typeOfContent

# TODO: permittedMediaTypes

# TODO: serializations

# TODO: contentInfo

# TODO: eventCat

# TODO: eventCatWithDef

# TODO: listOfEventCat

# TODO: listOfEventCatWithDef

# TODO: scheduleEntry


class ListOfURIsS(StringListAttribute):
    content_type = AnyURI


class AttributeListS(StringListAttribute):
    pass

# complex ######################################################################

# TODO: deliveryMetaData

# TODO: aggregatedRequest

# TODO: metaInformation

# TODO: primitiveContent


class FilterCriteria(OneM2MEntity):
    createdBefore = TimestampS()
    createdAfter = TimestampS()
    modifiedSince = TimestampS()
    unmodifiedSince = TimestampS()
    stateTagSmaller = Attribute(int)  # xs:positiveInteger
    stateTagBigger = Attribute(int)  # xs:nonNegativeInteger
    expireBefore = TimestampS()
    expireAfter = TimestampS()
    labels = StringListAttribute()
    resourceType = ListAttribute(ResourceTypeE)
    sizeAbove = Attribute(int)  # xs:nonNegativeInteger
    sizeBelow = Attribute(int)  # xs:positiveInteger
    contentType = UnicodeAttribute()  # m2m:typeOfContent
    attribute = ListAttribute()  # m2m:attribute
    filterUsage = EntityAttribute(FilterUsageE)
    limit = Attribute(int)  # xs:nonNegativeInteger

# TODO: attribute

# TODO: scheduleEntries

# TODO: actionStatus

# TODO: anyArgType

# TODO: resetArgsType

# TODO: rebootArgsType

# TODO: uploadArgsType

# TODO: downloadArgsType

# TODO: softwareInstallArgsType

# TODO: softwareUpdateArgsType

# TODO: softwareUninstallArgsType

# TODO: execReqArgsListType

# TODO: mgmtLinkRef

# TODO: childResourceRef

# TODO: responseTypeInfo

# TODO: operationResult


class LabeledResource(OneM2MResource):
    labels = LabelsS()


class ExpiringResource(OneM2MResource):
    expirationTime = TimestampS(mandatory=False)


class AccessControlPolicyIDHolder(OneM2MResource):
    accessControlPolicyIDs = StringListAttribute()


class SubscribableResource(OneM2MResource):
    pass


class AnnounceableResource(OneM2MResource):
    announceTo = ListOfURIsS()
    announcedAttribute = UnicodeAttribute()  # TODO


class AnnouncedResource(OneM2MResource):
    link = Attribute(AnyURI)


class ResourceC(LabeledResource):
    __child_types__ = ()

    typename = None

    resourceName = UnicodeAttribute(accesstype=Attribute.WO)

    resourceType = EntityAttribute(ResourceTypeE, accesstype=Attribute.RO)
    resourceID = IDS(accesstype=Attribute.RO)
    parentID = NhURIS(accesstype=Attribute.RO)

    lastModifiedTime = TimestampS(accesstype=Attribute.RO)
    creationTime = TimestampS(accesstype=Attribute.RO)

    childResource = ListAttribute()

    @property
    def name(self):
        return self.resourceName

    @property
    def id(self):
        return self.resourceID

    def __repr__(self):
        return "%s(path='%s', id='%s')" % (type(self).__name__, self.path,
                                           self.id)


ResourceC.childResource.content_type = ResourceC


class RegularResourceC(ResourceC, ExpiringResource,
                       AccessControlPolicyIDHolder):
    pass


class AnnounceableResourceC(RegularResourceC, AnnounceableResource):
    pass


class AnnouncedResourceC(RegularResourceC, AnnouncedResource):
    pass


class AnnounceableSubordinateResourceC(ResourceC, ExpiringResource,
                                       AnnounceableResource):
    pass


class AnnouncedSubordinateResourceC(ResourceC, ExpiringResource,
                                    AnnouncedResource):
    pass

# TODO: mgmtResource

# TODO: announcedMgmtResource


################################################################################
# requestPrimitive
################################################################################

class RequestPrimitive(OneM2MEntity):
    operation = EntityAttribute(OperationE)
    to = Attribute(AnyURI)
    from_ = IDS()
    requestIdentifier = RequestIDS()
    resourceType = EntityAttribute(ResourceTypeE)
    name = UnicodeAttribute()
    primitiveContent = UnicodeAttribute()  # m2m:primitiveContent
    role = UnicodeAttribute()  # xs:anyType
    originatingTimestamp = TimestampS()
    requestExpirationTimestamp = TimestampS()  # m2m::absRelTimestamp
    resultExpirationTimestamp = TimestampS()  # m2m::absRelTimestamp
    operationExecutionTime = TimestampS()  # m2m::absRelTimestamp
    responseType = UnicodeAttribute()  # m2m:responseTypeInfo
    resultPersistence = TimestampS()  # m2m::absRelTimestamp
    resultContent = UnicodeAttribute()  # m2m:resultContent
    eventCategory = UnicodeAttribute()  # m2m:eventCat
    deliveryAggregation = Attribute(bool)
    groupRequestIdentifier = UnicodeAttribute()
    filterCriteria = EntityAttribute(FilterCriteria)
    discoveryResultType = EntityAttribute(DiscResTypeE)


class AttributeList(OneM2MContentResource):
    typename = "attributeList"
    CONTENT = AttributeListS()


################################################################################
# responsePrimitive
################################################################################

class ResponsePrimitive(OneM2MEntity):
    responseStatusCode = UnicodeAttribute()  # m2m:responseStatusCode
    requestIdentifier = RequestIDS()
    primitiveContent = UnicodeAttribute()  # m2m:primitiveContent
    to = IDS()
    from_ = IDS()
    originatingTimestamp = TimestampS()
    resultExpirationTimestamp = TimestampS()  # m2m:absRelTimestamp
    eventCategory = UnicodeAttribute()  # m2m:eventCat


class Resource(OneM2MContentResource):
    pass


class URIList(OneM2MContentResource):
    typename = "URIList"
    CONTENT = ListOfURIsS()


class AggregatedResponse(OneM2MEntity):
    responsePrimitive = ListAttribute(ResponsePrimitive)


################################################################################
# notification
################################################################################

class OperationMonitorTypeC(OneM2MEntity):
    operation = UnicodeAttribute()  # m2m:operation
    originator = UnicodeAttribute()  # m2m:ID


class NotificationEventC(OneM2MEntity):
    representation = EntityAttribute(ResourceC)  # xs:anyType
    operationMonitor = EntityAttribute(OperationMonitorTypeC)
    notificationEventType = EntityAttribute(NotificationEventTypeE)


class Notification(OneM2MEntity):
    notificationEvent = EntityAttribute(NotificationEventC)
    verificationRequest = Attribute(bool)
    subscriptionDeletion = Attribute(bool)
    subscriptionReference = Attribute(AnyURI)
    creator = UnicodeAttribute()  # ID
    notificationForwardingURI = Attribute(AnyURI)


class AggregatedNotification(OneM2MEntity):
    """See TS-0004 Table 7.4.1.1-2"""

    notification = ListAttribute(Notification)


################################################################################
# subscription
################################################################################

class EventNotificationCriteria(OneM2MEntity):
    """See TS-0004 Table 6.3.2.3-1"""

    createdBefore = TimestampS()
    createdAfter = TimestampS()
    modifiedSince = TimestampS()
    unmodifiedSince = TimestampS()
    stateTagSmaller = Attribute(int)
    stateTagBigger = Attribute(int)
    expireBefore = TimestampS()
    expireAfter = TimestampS()
    sizeAbove = Attribute(int)
    sizeBelow = Attribute(int)
    operationMonitor = UnicodeAttribute()  # ListAttribute(m2m:operation)
    # attribute = Attribute(int)  # enum but to be defined in the standard
    attribute = UnicodeAttribute()  # ListAttribute(m2m:attribute)
    notificationEventType = ListAttribute(NotificationEventTypeE)


class BatchNotify(OneM2MEntity):
    pass  # TODO


class RateLimit(OneM2MEntity):
    pass  # TODO


class Subscription(RegularResourceC):
    """ See TS-0001 section 9.6.8
        See TS-0004 Table 7.3.7.1-3"""

    eventNotificationCriteria = EntityAttribute(EventNotificationCriteria)
    expirationCounter = Attribute(int)
    notificationURI = ListOfURIsS(mandatory=True)
    groupID = Attribute(AnyURI)
    notificationForwardingURI = Attribute(AnyURI)
    batchNotify = EntityAttribute(BatchNotify)
    rateLimit = EntityAttribute(RateLimit)
    preSubscriptionNotify = Attribute(int, accesstype=Attribute.WO,
                                      mandatory=False)
    pendingNotification = Attribute(PendingNotificationE)
    notificationStoragePriority = Attribute(int)
    latestNotify = Attribute(bool)
    notificationContentType = Attribute(NotificationContentTypeE)
    notificationEventCat = UnicodeAttribute()  # m2m:eventCat
    creator = IDS(accesstype=Attribute.WO, mandatory=False)
    subscriberURI = Attribute(AnyURI, accesstype=Attribute.WO, mandatory=False)

    __child_types__ = (
        # Schedule,
    )


################################################################################
# accessControlPolicy TODO
################################################################################

# class AccessControlLocationRegionC(OneM2MEntity):
#     latitude = Attribute(float)
#     longitude = Attribute(float)
#     radius = Attribute(float)
#     countryCode = Attribute(CountryCode)
#
#
# class AccessControlWindowsC(OneM2MEntity):
#     accessControlWindow = ListAttribute(str)
#
#
# class AccessControlIpAddressesC(OneM2MEntity):
#     accessControlIPAddr = ListAttribute(AnyURI)
#
#
# class AccessControlContexts(OneM2MEntity):
#     accessControlWindows = ListAttribute(AccessControlWindowsC)
#     accessControlIpAddresses = ListAttribute(AccessControlIpAddressesC)
#     accessControlLocationRegions = ListAttribute(AccessControlLocationRegionC)
#
#
# class AccessControlRule(OneM2MEntity):
#     accessControlOriginators = ListAttribute(AnyURI)
#     accessControlContexts = EntityAttribute(AccessControlContextsC)
#     accessControlOperations = ListAttribute(AccessControlOperationE)


class AccessControlPolicy(AnnounceableSubordinateResourceC,
                          SubscribableResource):
    # privileges = ListAttribute(AccessControlRule)
    # selfPrivileges = ListAttribute(AccessControlRule)

    __child_types__ = (
        Subscription,
    )


class AccessControlPolicyAnnc(AnnouncedSubordinateResourceC,
                              SubscribableResource):
    # privileges = ListAttribute(AccessControlRule)
    # selfPrivileges = ListAttribute(AccessControlRule)

    __child_types__ = (
        Subscription,
    )


################################################################################
# remoteCSE
################################################################################

class RemoteCSE(AnnounceableResourceC, SubscribableResource):
    """See TS-0001 section 9.6.4"""

    cseType = Attribute(CSETypeIDE, accesstype=Attribute.WO, mandatory=False)
    pointOfAccess = StringListAttribute()
    CSEBase = UnicodeAttribute(accesstype=Attribute.WO)
    CSE_ID = UnicodeAttribute(accesstype=Attribute.WO)  # TODO: CSE-ID (minus!)
    M2M_Ext_ID = UnicodeAttribute()  # TODO: M2M-Ext-ID (minus!)
    Trigger_Recipient_ID = UnicodeAttribute()  # TODO: Trigger-Recipient-ID
    requestReachability = Attribute(bool)
    nodeLink = UnicodeAttribute()

    __child_types__ = (
        Subscription,
    )


class RemoteCSEAnnc(AnnouncedResourceC, SubscribableResource):
    cseType = Attribute(CSETypeIDE, accesstype=Attribute.WO, mandatory=False)
    pointOfAccess = StringListAttribute()
    CSEBase = UnicodeAttribute(accesstype=Attribute.WO)
    CSE_ID = UnicodeAttribute(accesstype=Attribute.WO)  # TODO: CSE-ID (minus!)
    requestReachability = Attribute(bool)
    nodeLink = UnicodeAttribute()

    __child_types__ = (
        Subscription,
        # TODO
    )


################################################################################
# contentInstance
################################################################################

class ContentInstance(AnnounceableSubordinateResourceC,
                      SubscribableResource):
    """See TS-0001 section 9.6.7"""

    stateTag = UnicodeAttribute(accesstype=Attribute.RO)
    creator = UnicodeAttribute()        # m2m:ID
    # contentInfo = typeOfContent(:EncodingType)
    # typeOfContent => Media Types
    # ex: application/json:1
    contentInfo = UnicodeAttribute()    # m2m:contentInfo
    contentSize = Attribute(int, accesstype=Attribute.RO)
    ontologyRef = UnicodeAttribute(accesstype=Attribute.WO)
    content = Attribute(bytes, accesstype=Attribute.WO, mandatory=True)

    __child_types__ = (
        Subscription,
    )


class ContentInstanceAnnc(AnnouncedSubordinateResourceC):
    stateTag = UnicodeAttribute(accesstype=Attribute.RO)
    contentInfo = UnicodeAttribute(EncodingTypeE)    # m2m:contentInfo
    contentSize = Attribute(int, accesstype=Attribute.WO)
    ontologyRef = UnicodeAttribute(accesstype=Attribute.WO)
    content = Attribute(bytes, accesstype=Attribute.WO, mandatory=True)


################################################################################
# container
################################################################################

class Container(AnnounceableResourceC, SubscribableResource):
    """See TS-0001 section 9.6.6"""

    stateTag = UnicodeAttribute(accesstype=Attribute.RO)
    creator = UnicodeAttribute()
    maxNrOfInstances = Attribute(int)
    maxByteSize = Attribute(int)
    maxInstanceAge = UnicodeAttribute(mandatory=False)  # todo
    currentNrOfInstances = Attribute(int, accesstype=Attribute.RO)
    currentByteSize = Attribute(int, accesstype=Attribute.RO)
    locationID = UnicodeAttribute()
    ontologyRef = UnicodeAttribute()
    latest = Attribute(ContentInstance, mandatory=False)
    oldest = Attribute(ContentInstance, mandatory=False)

    __child_types__ = (
        ContentInstance,
        Subscription,
    )

Container.__child_types__ = (
    ContentInstance,
    Container,
    Subscription,
)


class ContainerAnnc(AnnouncedResourceC, SubscribableResource):

    stateTag = UnicodeAttribute(accesstype=Attribute.RO)
    maxNrOfInstances = Attribute(int)
    maxByteSize = Attribute(int)
    maxInstanceAge = UnicodeAttribute(mandatory=False)  # todo
    currentNrOfInstances = Attribute(int, accesstype=Attribute.RO)
    currentByteSize = Attribute(int, accesstype=Attribute.RO)
    locationID = UnicodeAttribute()
    ontologyRef = UnicodeAttribute()
    latest = Attribute(ContentInstance, mandatory=False)

    __child_types__ = (
        ContentInstance,
        ContentInstanceAnnc,
        Container,
        Subscription,
    )

ContainerAnnc.__child_types__ = (
    ContentInstance,
    ContentInstanceAnnc,
    Container,
    ContainerAnnc,
    Subscription,
)


################################################################################
# AE
################################################################################

class AE(AnnounceableResourceC, SubscribableResource):
    """See TS-0001 section 9.6.5"""

    typename = "AE"

    appName = UnicodeAttribute()
    App_ID = UnicodeAttribute(accesstype=Attribute.WO, mandatory=True)
    AE_ID = UnicodeAttribute(accesstype=Attribute.RO)
    pointOfAccess = StringListAttribute()
    ontologyRef = UnicodeAttribute()
    nodeLink = UnicodeAttribute(accesstype=Attribute.RO)
    requestReachability = Attribute(bool, mandatory=True)
    contentSerialization = UnicodeAttribute()  # TODO m2m:serializations

    __child_types__ = (
        Container,
        # Group,
        Subscription,
        # AccessControlPolicy,
        # PollingChannel,
        # Schedule,
    )


class AEAnnc(AnnouncedResourceC, SubscribableResource):

    typename = "AEAnnc"

    appName = UnicodeAttribute(accesstype=Attribute.WO)
    App_ID = UnicodeAttribute()
    AE_ID = UnicodeAttribute()
    pointOfAccess = StringListAttribute()
    ontologyRef = UnicodeAttribute()
    nodeLink = UnicodeAttribute()
    requestReachability = Attribute(bool)

    __child_types__ = (
        Container,
        ContainerAnnc,
        # Group,
        # GroupAnnc,
        Subscription,
        # AccessControlPolicy,
        # AccessControlPolicyAnnc,
        # PollingChannel,
        # Schedule,
    )


################################################################################
# CSEBase
################################################################################

class CSEBase(ResourceC, SubscribableResource, AccessControlPolicyIDHolder):
    """See TS-0001 section 9.6.3"""

    typename = "CSEBase"

    cseType = Attribute(CSETypeIDE, accesstype=Attribute.WO)
    CSE_ID = UnicodeAttribute(accesstype=Attribute.WO)  # TODO: CSE-ID (minus!)
    supportedResourceType = StringListAttribute(content_type=ResourceTypeE,
                                                accesstype=Attribute.RO)
    pointOfAccess = StringListAttribute()
    nodeLink = UnicodeAttribute()

    __child_types__ = (
        RemoteCSE,
        # Node,
        AE,
        Container,
        # Group,
        AccessControlPolicy,
        Subscription,
        # MgmtCmd,
        # LocationPolicy,
        # StatsConfig,
        # StatsCollect,
        # Request,
        # Delivery,
        # Schedule,
        # M2mServiceSubscriptionProfile,
    )


################################################################################
# misc
################################################################################

long_to_short_attribute_mapping = {
    "accessControlPolicyIDs": "acpi",
    "announcedAttribute": "aa",
    "announceTo": "at",
    "creationTime": "ct",
    "expirationTime": "et",
    "labels": "lbl",
    "lastModifiedTime": "lt",
    "parentID": "pi",
    "resourceID": "ri",
    "resourceType": "ty",
    "stateTag": "st",
    "resourceName": "rn",
    "privileges": "pv",
    "selfPrivileges": "pvs",
    "App-ID": "api",
    "AE-ID": "aei",
    "appName": "apn",
    "pointOfAccess": "poa",
    "ontologyRef": "or",
    "nodeLink": "nl",
    "contentSerialization": "csz",
    "creator": "cr",
    "maxNrOfInstances": "mni",
    "maxByteSize": "mbs",
    "maxInstanceAge": "mia",
    "currentNrOfInstances": "cni",
    "currentByteSize": "cbs",
    "locationID": "li",
    "contentInfo": "cnf",
    "contentSize": "cs",
    "primitiveContent": "pc",
    "content": "con",
    "cseType": "cst",
    "CSE-ID": "csi",
    "supportedResourceType": "srt",
    "notificationCongestionPolicy": "ncp",
    "source": "sr",
    "target": "tg",
    "lifespan": "ls",
    "eventCat": "ec",
    "deliveryMetaData": "dmd",
    "aggregatedRequest": "arq",
    "eventID": "evi",
    "eventType": "evt",
    "evenStart": "evs",
    "eventEnd": "eve",
    "operationType": "opt",
    "dataSize": "ds",
    "execStatus": "exs",
    "execResult": "exr",
    "execDisable": "exd",
    "execTarget": "ext",
    "execMode": "exm",
    "execFrequency": "exf",
    "execDelay": "exy",
    "execNumber": "exn",
    "execReqArgs": "exra",
    "execEnable": "exe",
    "memberType": "mt",
    "currentNrOfMembers": "cnm",
    "maxNrOfMembers": "mnm",
    "memberIDs": "mid",
    "membersAccessControlPolicyIDs": "macp",
    "memberTypeValidated": "mtv",
    "consistencyStrategy": "csy",
    "groupName": "gn",
    "locationSource": "los",
    "locationUpdatePeriod": "lou",
    "locationTargetId": "lot",
    "locationServer": "lor",
    "locationContainerID": "loi",
    "locationContainerName": "lon",
    "locationStatus": "lost",
    "serviceRoles": "svr",
    "description": "dc",
    "cmdType": "cmt",
    "mgmtDefinition": "mgd",
    "objectIDs": "onis",
    "objectPaths": "obps",
    "nodeID": "ni",
    "hostedCSELink": "hcl",
    "CSEBase": "cb",
    "M2M-Ext-ID": "mei",
    "Trigger-Recipient-ID": "tri",
    "requestReachability": "rr",
    "originator": "og",
    "metaInformation": "mi",
    "requestStatus": "rs",
    "operationResult": "ol",
    "operation": "opn",
    "requestID": "rid",
    "scheduleElement": "se",
    "deviceIdentifier": "di",
    "ruleLinks": "rlk",
    "statsCollectID": "sci",
    "collectingEntityID": "cei",
    "collectedEntityID": "cdi",
    "devStatus": "ss",
    "statsRuleStatus": "srs",
    "statModel": "sm",
    "collectPeriod": "cp",
    "eventNotificationCriteria": "enc",
    "expirationCounter": "exc",
    "notificationURI": "nu",
    "groupID": "gpi",
    "notificationForwardingURI": "nfu",
    "batchNotify": "bn",
    "rateLimit": "rl",
    "preSubscriptionNotify": "psn",
    "pendingNotification": "pn",
    "notificationStoragePriority": "nsp",
    "latestNotify": "ln",
    "notificationContentType": "nct",
    "notificationEventCat": "nec",
    "subscriberURI": "su",
    "version": "vr",
    "URL": "url",
    "update": "ud",
    "updateStatus": "uds",
    "install": "in",
    "uninstall": "un",
    "installStatus": "ins",
    "activate": "act",
    "deactivate": "dea",
    "activeStatus": "acts",
    "memAvailable": "mma",
    "memTotal": "mmt",
    "areaNwkType": "ant",
    "listOfDevices": "idv",
    "devId": "dvd",
    "devType": "dvt",
    "areaNwkId": "awi",
    "sleepInterval": "sli",
    "sleepDuration": "sld",
    "listOfNeighbors": "lnh",
    "batteryLevel": "btl",
    "batteryStatus": "bts",
    "deviceLabel": "dlb",
    "manufacturer": "man",
    "model": "mod",
    "deviceType": "dty",
    "fwVersion": "fwv",
    "swVersion": "swv",
    "hwVersion": "hwv",
    "capabilityName": "can",
    "attached": "att",
    "capabilityActionStatus": "cas",
    "enable": "ena",
    "disable": "dis",
    "currentState": "cus",
    "reboot": "rbo",
    "factoryReset": "far",
    "logTypeId": "lgt",
    "logData": "lgd",
    "logActionStatus": "lgs",
    "logStatus": "lgst",
    "logStart": "lga",
    "logStop": "lgo",
    "firmwareName": "fwnnam",
    "softwareName": "swn",
    "cmdhPolicyName": "cpn",
    "mgmtLink": "cmlk",
    "activeCmdhPolicyLink": "acmlk",
    "order": "od",
    "defEcValue": "dev",
    "requestOrigin": "ror",
    "requestContext": "rct",
    "requestContextNotification": "rcn",
    "requestCharacteristics": "rch",
    "applicableEventCategories": "aecs",
    "applicableEventCategory": "aec",
    "defaultRequestExpTime": "dget",
    "defaultResultExpTime": "dset",
    "defaultOpExecTime": "doet",
    "defaultRespPersistence": "drp",
    "defaultDelAggregation": "dda",
    "limitsEventCategory": "lec",
    "limitsRequestExpTime": "lget",
    "limitsResultExpTime": "lset",
    "limitsOpExecTime": "loet",
    "limitsRespPersistence": "lrp",
    "limitsDelAggregation": "lda",
    "targetNetwork": "ttn",
    "minReqVolume": "mrv",
    "backOffParameters": "bop",
    "otherConditions": "ohc",
    "maxBufferSize": "mbfs",
    "storagePriority": "sgp",
    "applicableCredIDs": "apci",
    "allowedApp-IDs": "aai",
    "allowedAEs": "aae"
}

short_to_long_attribute_mapping = {v: k for k, v in
                                   long_to_short_attribute_mapping.items()}


def get_long_attribute_name(n):
    return short_to_long_attribute_mapping.get(n)


def get_short_attribute_name(n):
    return long_to_short_attribute_mapping.get(n)

long_to_short_resource_mapping = {
    "accessControlPolicy": "acp",
    "accessControlPolicyAnnc": "acpA",
    "AE": "ae",
    "AEAnnc": "aeA",
    "container": "cnt",
    "containerAnnc": "cntA",
    "latest": "la",
    "oldest": "ol",
    "contentInstance": "cin",
    "contentInstanceAnnc": "cinA",
    "CSEBase": "cb",
    "delivery": "dlv",
    "eventConfig": "evcg",
    "execInstance": "exin",
    "fanOutPoint": "fopt",
    "group": "grp",
    "groupAnnc": "grpA",
    "locationPolicy": "lcp",
    "locationPolicyAnnc": "lcpA",
    "m2mServiceSubscriptionProfile": "mssp",
    "mgmtCmd": "mgc",
    "mgmtObj": "mgo",
    "mgmtObjAnnc": "mgoA",
    "node": "nod",
    "nodeAnnc": "nodA",
    "pollingChannel": "pch",
    "pollingChannelURI": "pcu",
    "remoteCSE": "csr",
    "remoteCSEAnnc": "csrA",
    "request": "req",
    "schedule": "sch",
    "scheduleAnnc": "schA",
    "serviceSubscribedAppRule": "asar",
    "serviceSubscribedNode": "svsn",
    "statsCollect": "stcl",
    "statsConfig": "stcg",
    "subscription": "sub",
    "firmware": "fwr",
    "firmwareAnnc": "fwrA",
    "software": "swr",
    "softwareAnnc": "swrA",
    "memory": "mem",
    "memoryAnnc": "memA",
    "areaNwkInfo": "ani",
    "areaNwkInfoAnnc": "aniA",
    "areaNwkDeviceInfo": "andi",
    "areaNwkDeviceInfoAnnc": "andiA",
    "battery": "bat",
    "batteryAnnc": "batA",
    "deviceInfo": "dvi",
    "deviceInfoAnnc": "dviA",
    "deviceCapability": "dvc",
    "deviceCapabilityAnnc": "dvcA",
    "reboot": "rbo",
    "rebootAnnc": "rboA",
    "eventLog": "evl",
    "eventLogAnnc": "evlA",
    "cmdhPolicy": "cmp",
    "activeCmdhPolicy": "acmp",
    "cmdhDefaults": "cmdf",
    "cmdhDefEcValue": "cmdv",
    "cmdhEcDefParamValues": "cmpv",
    "cmdhLimits": "cml",
    "cmdhNetworkAccessRules": "cmnr",
    "cmdhNwAccessRule": "cmwr",
    "cmdhBuffer": "cmbf"
}

short_to_long_resource_mapping = {v: k for k, v in
                                  long_to_short_resource_mapping.items()}


def get_long_resource_name(n):
    return short_to_long_resource_mapping.get(n)


def get_short_resource_name(n):
    return long_to_short_resource_mapping.get(n)


long_to_short_member_mapping = {
    "createdBefore": "crb",
    "createdAfter": "cra",
    "modifiedSince": "ms",
    "unmodifiedSince": "us",
    "stateTagSmaller": "sts",
    "stateTagBigger": "stb",
    "expireBefore": "exb",
    "expireAfter": "exa",
    "labels": "lbl",
    "resourceType": "ty",
    "sizeAbove": "sza",
    "sizeBelow": "szb",
    "contentType": "cty",
    "limit": "lim",
    "attribute": "atr",
    "notificationEventType": "net",
    "operationMonitor": "om",
    "representation": "rep",
    "filterUsage": "fu",
    "eventCatType": "ect",
    "eventCatNo": "ecn",
    "number": "num",
    "duration": "dur",
    "notification": "sgn",
    "notificationEvent": "nev",
    "verificationRequest": "vrq",
    "subscriptionDeletion": "sud",
    "subscriptionReference": "sur",
    "creator": "cr",
    "notificationForwardingURI": "nfu",
    "operation": "opr",
    "originator": "org",
    "accessId": "aci",
    "MSISDN": "msd",
    "action": "acn",
    "status": "sus",
    "childResource": "ch",
    "accessControlRule": "acr",
    "accessControlOriginators": "acor",
    "accessControlOperations": "acop",
    "accessControlContexts": "acco",
    "accessControWindow": "actw",
    "accessControlIpAddresses": "acip",
    "ipv4Addresses": "ipv4",
    "ipv6Addresses": "ipv6",
    "accessControlLocationRegion": "aclr",
    "countryCode": "accc",
    "circRegion": "accr",
    "name": "nm",
    "value": "val",
    "type": "typ",
    "maxNrOfNotify": "mnn",
    "timeWindow": "tww",
    "scheduleEntry": "sce",
    "aggregatedNotification": "agn",
    "attributeList": "atrl",
    "aggregatedResponse": "agr",
    "resource": "rce",
    "URIList": "uril",
    "anyArg": "any",
    "fileType": "ftyp",
    "URL": "url",
    "username": "unm",
    "password": "pwd",
    "fileSize": "fsi",
    "targetFile": "tgf",
    "delaySeconds": "dss",
    "successURL": "surl",
    "startTime": "stt",
    "completeTime": "cpt",
    "UUID": "uuid",
    "executionEnvRef": "eer",
    "version": "vr",
    "reset": "rst",
    "reboot": "rbo",
    "upload": "uld",
    "download": "dld",
    "softwareInstall": "swin",
    "softwareUpdate": "swup",
    "softwareUninstall": "swun",
    "tracingOption": "tcop",
    "tracingInfo": "tcin",
    "responseTypeValue": "rtv",
    "notificationURI": "nu"
}

short_to_long_member_mapping = {v: k for k, v in
                                long_to_short_member_mapping.items()}


def get_long_member_name(n):
    return short_to_long_member_mapping.get(n)


def get_short_member_name(n):
    return long_to_short_member_mapping.get(n)

long_to_short_root_mapping = {
    "requestPrimitive": "rqp",
    "responsePrimitive": "rsp"
}

short_to_long_root_mapping = {v: k for k, v in
                              long_to_short_root_mapping.items()}


def get_long_root_name(n):
    return short_to_long_root_mapping.get(n)


def get_short_root_name(n):
    return long_to_short_root_mapping.get(n)

long_to_short_parameter_mapping = {
    "operation": "op",
    "to": "to",
    "from": "fr",
    "requestIdentifier": "rqi",
    "resourceType": "ty",
    "primitiveContent": "pc",
    "role": "rol",
    "originatingTimestamp": "ot",
    "requestExpirationTimestamp": "rqet",
    "resultExpirationTimestamp": "rset",
    "operationExecutionTime": "oet",
    "responseType": "rt",
    "resultPersistence": "rp",
    "resultContent": "rcn",
    "eventCategory": "ec",
    "deliveryAggregation": "da",
    "groupRequestIdentifier": "gid",
    "filterCriteria": "fc",
    "discoveryResultType": "drt",
    "responseStatusCode": "rsc"
}

short_to_long_parameter_mapping = {v: k for k, v in
                                   long_to_short_parameter_mapping.items()}


def get_long_parameter_name(n):
    return short_to_long_parameter_mapping.get(n)


def get_short_parameter_name(n):
    return long_to_short_parameter_mapping.get(n)

_all_types = {k: v for k, v in globals().iteritems()
              if issubclass(v, OneM2MEntity) and not v.__subclasses__()}

_all_types_short = {}
_all_types_long = {}

for k, v in _all_types.iteritems():
    if get_short_resource_name(k):
        long_name = k
        short_name = get_short_resource_name(k)
    elif get_short_attribute_name(k):
        long_name = k
        short_name = get_short_attribute_name(k)
    elif get_short_member_name(k):
        long_name = k
        short_name = get_short_member_name(k)
    elif get_short_root_name(k):
        long_name = k
        short_name = get_short_root_name(k)
    elif get_short_resource_name(k[0].lower() + k[1:]):
        long_name = k[0].lower() + k[1:]
        short_name = get_short_resource_name(long_name)
    elif get_short_attribute_name(k[0].lower() + k[1:]):
        long_name = k[0].lower() + k[1:]
        short_name = get_short_attribute_name(long_name)
    elif get_short_member_name(k[0].lower() + k[1:]):
        long_name = k[0].lower() + k[1:]
        short_name = get_short_member_name(long_name)
    elif get_short_root_name(k[0].lower() + k[1:]):
        long_name = k[0].lower() + k[1:]
        short_name = get_short_root_name(long_name)
    else:
        continue
    _all_types_short[short_name] = v
    _all_types_long[long_name] = v


_resource_types = {k: v for k, v in _all_types.iteritems()
                   if issubclass(v, ResourceC)}

_resource_types_short = {}
_resource_types_long = {}

for k, v in _resource_types.iteritems():
    if get_short_resource_name(k):
        long_name = k
        short_name = get_short_resource_name(k)
    elif get_short_resource_name(k[0].lower() + k[1:]):
        long_name = k[0].lower() + k[1:]
        short_name = get_short_resource_name(long_name)
    else:
        continue
    _resource_types_short[short_name] = v
    _resource_types_long[long_name] = v


def get_onem2m_type(typename):
    try:
        try:
            return _all_types_short[typename]
        except KeyError:
            return _all_types_long[typename]
    except KeyError:
        raise ModelTypeError("Not a valid type: %s" % (typename,))


def get_onem2m_resource_type(typename):
    try:
        try:
            return _resource_types_short[typename]
        except KeyError:
            return _resource_types_long[typename]
    except KeyError:
        raise ModelTypeError("Not a valid resource type: %s" % (typename,))


def get_onem2m_types():
    return _all_types.values()


def get_onem2m_resource_types():
    return _resource_types.values()
