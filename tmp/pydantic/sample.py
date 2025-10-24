from gsp_messages import BufferType, Buffer, CanvasCreate, CanvasSetDpi, CanvasSetSize, Pixels, Transform, TransformLinkOperator, Viewport

# =============================================================================
# Create a canvas
# =============================================================================

create_canvas_msg = CanvasCreate(
    message_id=1,
    canvas_uuid='123e4567-e89b-12d3-a456-426614174000',
    width=800,
    height=600,
    dpi=96.0
)

set_canvas_dpi_msg = CanvasSetDpi(
    message_id=2,
    canvas_uuid=create_canvas_msg.canvas_uuid,
    dpi=120.0,
)

# =============================================================================
# Viewport
# =============================================================================

create_viewport_msg = Viewport(
    message_id=3,
    viewport_uuid='223e4567-e89b-12d3-a456-426614174001',
    canvas_uuid=create_canvas_msg.canvas_uuid,
    x=0,
    y=0,
    width=400,
    height=300
)

# =============================================================================
# Pixels
# =============================================================================

buffer_position_msg = Buffer(
    message_id=5,
    buffer_uuid='423e4567-e89b-12d3-a456-426614174003',
    count=4,
    type=BufferType.int32,
    data=b'\x00\x00\x00\x00\x00\x00\x80\x3f\x00\x00\x00\x00\x00\x00\x00\x40'
)

buffer_color_msg = Buffer(
    message_id=6,
    buffer_uuid='523e4567-e89b-12d3-a456-426614174004',
    count=4,
    type=BufferType.float32,
    data=b'\x00\x00\x00\x00\x00\x00\x80\x3f\x00\x00\x00\x00\x00\x00\x00\x40'
)

buffer_groups_msg = Buffer(
    message_id=7,
    buffer_uuid='623e4567-e89b-12d3-a456-426614174005',
    count=2,
    type=BufferType.int32,
    data=b'\x00\x00\x00\x00\x02\x00\x00\x00'
)   

create_pixels_msg = Pixels(
    message_id=4,
    viewport_uuid=create_viewport_msg.viewport_uuid,
    positions=buffer_position_msg.buffer_uuid,
    colors=buffer_color_msg.buffer_uuid,
    groups=buffer_groups_msg.buffer_uuid,
)


